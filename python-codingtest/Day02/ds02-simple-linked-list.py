class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

# 전역변수
memory = [] # list()
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

def printNodes(start):
    current = start
    if current == None:
        return

    print(current.data, end=' -> ')

    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end=' -> ')

# 노드 추가
def insertNode(finddata, insertdata):
    global memory, pre, current, head

    if head.data == finddata:   # 첫노드앞
        node = Node()
        node.data = insertdata
        node.link = head
        head = node
        return
    
    current = head # 제일 앞으로
    while current.link != None: # 중간노드
        pre = current
        current = current.link

        if current.data == finddata:
            node = Node()
            node.data = insertdata
            node.link = current
            pre.link = node
            return 
    # current.link == None 까지 온것
    node = Node()
    node.data = insertdata
    current.link = node
    return

# 노드 삭제
def deleteNode(deleteData):
    global memory, pre, current, head

    if head.data == deleteData:  # 첫번재 노드 삭제:
        current = head
        head = head.link# 두번재 노드로 변경
        del(current)
        return
    
    current = head
    while current.link != None:
        pre = current # 모두 첫번재 노드 가리킴
        current = current.link  # 두번재 노드를 가르킴
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

# 노드 검색
def findNode(findData):
    global memory, pre, current, head

    current = head #첫번째 노드부터
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link  # 다음노드
        if current.data == findData:
            return current
    
    return Node()   # 빈 노드 반환


if __name__ == '__main__':

    node = Node()               # 첫번째 노드
    node.data = dataArray[0]    # 다현
    head = node                 # node랑 head의 가르키는 주소는 같음.
    memory.append(node)
                                
    for data in dataArray[1:]:  # for 첫번째 실행 결과
        pre = node              # pre랑 node, head의  주소는 같음. 완전히 같다는 뜻
        node = Node()           # node는 새로운 주소를 가지게됨 (두번째 노드).
        node.data = data         # 정연, 쯔위, 사나, 지효 순
        pre.link = node         # pre.link에 두번째 노드가 들어감. pre와 head가 같기때문에 head.link도 바뀜
        memory.append(node)
        # for 두번째 실행 결과
        # pre랑 두번재 node의 주소가 같음. 완전히 같다는 뜻.
        # node는 새로운 주소를 가지게됨 (세번째 노드).
        # 쯔위
        # pre.link에 세번째 노드가 들어감. 
        # 결론->  head는 첫번재 노드 그대로. head.link에는 두번재 노드. pre는 두번재 노드 pre.link는 세번째 노드. node는 세번재 노드

    printNodes(head)    # 전체출력

    print('노드 추가----')
    insertNode('재남', '문별')  # 맨마지막에 노드 추가
    printNodes(head)

    insertNode('사나', '솔라')  # 중간 노드추가
    printNodes(head)

    insertNode('다현', '화사')  # 맨앞에 화사노드 추가  
    printNodes(head)

    print('노드 삭제----')

    deleteNode('화사')
    printNodes(head)

    deleteNode('지효')
    printNodes(head)

    deleteNode('재남')  # 데이터 삭재X
    printNodes(head)

    print('노드 검색----')

    result = findNode('정연')

    if result.data == '정연':
        print(result.data)
    else:
        print('검색한 데이터 없습니다')

    result = findNode('재남')
    print(result.data)



