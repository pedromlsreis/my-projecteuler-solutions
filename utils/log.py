# Python packages
from pathlib import Path
import re

# Third-party packages
import numpy as np
import pandas as pd


class MarkdownLogger:
    """
    A logger that enables me to efficiently save the running times for each problem
    in a big, beautiful markdown table.
    """
    def __init__(self, directory='../..', filename='Records.md', last_problem=723):
        self.last_problem = last_problem
        self.directory = Path(directory)
        self.filename  = Path(filename)
        self.path_to_file = self.directory / self.filename
        if self.path_to_file.exists():
            self.read_file(self.path_to_file)
        else:
            self.create_file()
            self.save_file(self.path_to_file)


    def create_file(self):
        self.records = pd.DataFrame(columns=['Solved', 'Time(s)', 'Solution', 'Language'],
                                    index=range(1, self.last_problem + 1))
        self.records['Solved']   = 0
        self.records['Solved']   = self.records['Solved'].astype(np.int8)
        self.records['Time(s)']  = -1.0
        self.records['Time(s)']  = self.records['Time(s)'].astype(float)
        self.records['Solution'] = '-'
        self.records['Language'] = '-'
        self.records['Language'] = self.records['Language'].astype(str)
    

    def read_file(self, src_path=str):
        with open(self.path_to_file, 'r') as f:
            self.records = f.readlines()
        
        index = None
        for n, line in enumerate(self.records):
            if line.startswith('|-'):
                index = n
            
        if not index:
            raise Exception(f'{src_path} does not contain a markdown table')
        
        white_patt = re.compile(r'\s')
        columns = self.records[index - 1]
        columns = re.sub(white_patt, '', columns).split('|')[1:-1]
        self.records = self.records[index+1:]
        corr_records = np.zeros((1, len(columns)))
        for line in self.records:
            corr_records = np.append(corr_records, [re.sub(white_patt, '', line).split('|')[1:-1]], axis=0)

        self.records = pd.DataFrame(corr_records[1:], columns=columns, index=range(1, self.last_problem + 1))
        self.records.index.name = 'Problem'

        
    def save_file(self, dst_path=str):
        with open(dst_path, 'w') as f:
            f.write(self.records.to_markdown())
        

    def add_problem(self, solution, problem_id=int, duration=float, language='Python'):
        self.records = self.records.loc[:, ['Solved', 'Time(s)', 'Solution', 'Language']]
        self.records.index.name = 'Problem'
        self.records.loc[problem_id, 'Solution'] = solution
        self.records.loc[problem_id, 'Time(s)']  = float(duration)
        self.records.loc[problem_id, 'Language'] = language
        self.records.loc[problem_id, 'Solved']   = 1
        self.records['Time(s)'] = self.records['Time(s)'].astype(float)
        self.save_file(self.path_to_file)


    def remove_problem(self, problem_id=int):
        self.records = self.records.loc[:, ['Solved', 'Time(s)', 'Solution', 'Language']]
        self.records.loc[problem_id, 'Solution'] = '-'
        self.records.loc[problem_id, 'Time(s)']  = float(-1.0)
        self.records.loc[problem_id, 'Language'] = '-'
        self.records.loc[problem_id, 'Solved']   = 0
        self.save_file(self.path_to_file)
