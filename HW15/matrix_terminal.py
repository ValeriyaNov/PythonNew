import  argparse
from matrix import Matrix
from convert import convert_format

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Получаем операцию над двумя матрицами")
    parser.add_argument('-m_1',  type = str)
    parser.add_argument('-m_2',  type = str )
    parser.add_argument('-operation', type=str, default='+')
    
    args = parser.parse_args()
    
    m_1 = convert_format(args.m_1)
   
    m_2 = convert_format(args.m_2)
   

    if args.operation == '+':
        print(f'СЛОЖЕНИЕ: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) + Matrix(m_2)} '))
    elif  args.operation == '*':
        print(f'УМНОЖЕНИЕ: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) * Matrix(m_2)} '))
    elif args.operation == '=':
        print(f'РАВЕНСТВО: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) == Matrix(m_2)} '))
    else:
        print(f'Такая операция {args.operation} над матрицами не предусмотрена!')

    # примеры вызова  из командной строки:
    #при написании матрицы для перехода на новую строку ставим "а", также в конце аргумента ставим "а"
    # python matrix_terminal.py -m_1=124a -m_2=124a
    # python matrix_terminal.py -m_1=124a888а999 -m_2=124a999а555а -operation=*
    # python matrix_terminal.py -m_1=124a -m_2=124a 