import os
import csv

def main():
    current_dir = os.path.dirname(__file__)
    file_name = 'test.csv'
    target_dir = os.path.join(current_dir, '../log/')
    if not os.path.exists(target_dir):
        os.makedirs(name=target_dir)
        with open(os.path.join(target_dir, file_name), mode='w') as f:
            writer = csv.writer(f)
            header = ['username', 'password']
            writer.writerow(header)
            writer.writerow(['testuser', 'testpass'])
    else:
        with open(os.path.join(target_dir, file_name), mode='w') as f:
            writer = csv.writer(f)
            writer.writerow(['testuser', 'testpass'])
    
if __name__ == '__main__':
    main()