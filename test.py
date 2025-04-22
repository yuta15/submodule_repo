import os
import csv

def main():
    file_path = 'test.csv'
    print(os.getcwd())
    with open(file_path, mode='w') as f:
        writer = csv.writer(f)
        header = ['username', 'password']
        writer.writerow(header)
        writer.writerow(['testuser', 'testpass'])
    
    
if __name__ == '__main__':
    main()