class Stack:

    id = 0

    def __init__(self, string):
        self.string = string[::-1]
        self.id = Stack.id + 1
        Stack.id += 1

    def is_empty(self) -> bool:
        if self.string:
            return True
        else:
            return False

    def push(self, new_element) -> None:
        for index, element in enumerate(self.string):
            if index == 0:
                continue
            element_stack = element + self.string[index - 1]

            if element_stack in ['{}', '[]', '()']:
                self.string = self.string[:index] + new_element[::-1] + self.string[index:]
                break

    def pop(self) -> str:
        for index, element in enumerate(self.string):
            if index == 0:
                continue
            element_stack = element + self.string[index - 1]

            if element_stack in ['{}', '[]', '()']:
                first_index = index - 1
                second_index = index + 1
                self.string = self.string[:first_index] + self.string[second_index:]
                return element_stack

    def peek(self) -> str:
        for index, element in enumerate(self.string):
            if index == 0:
                continue
            element_stack = element + self.string[index - 1]

            if element_stack in ['{}', '[]', '()']:
                return element_stack

    def size(self) -> int:
        count_tuple = self.string.count('(') + self.string.count(')')
        count_list = self.string.count('[') + self.string.count(']')
        count_dict = self.string.count('{') + self.string.count('}')
        if count_tuple % 2 == 0 and count_list % 2 == 0 and count_dict % 2 == 0:
            count = int((count_tuple + count_list + count_dict) / 2)
            return count


list_of_strings = [
    '',
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
]


def main():
    for string in list_of_strings:
        object = Stack(string)
        if object.is_empty():
            checking_the_balance(object)
        else:
            print(f'Стек №{object.id} пустой')


def checking_the_balance(object: Stack) -> None:
    text = object.string[::-1]
    if object.size():
        for _ in range(object.size()):
            if object.peek():
                object.pop()
            else:
                print(f'Стек №{object.id}', 'Несбалансированно ', text)
                break
        else:
            print(f'Стек №{object.id}', 'Сбалансированно ', text)
    else:
        print(f'Стек №{object.id}', 'Несбалансированно ', text)


if __name__ == '__main__':
    main()