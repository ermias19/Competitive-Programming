class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        count = 0

        while cur.next != None:

            cur = cur.next

            count += 1
        cur.next = new_node
     

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elem = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)

    def get(self, index):
        cur_index = 0
        cur = self.head

        while True:
            cur = cur.next
            if cur_index == index:
                return cur.data
            cur_index += 1

    def delete(self,index):
        cur = self.head
        cur_index=0

        while cur.next!=None and index>cur_index :
            # print("minsdn nw yemilwn neger enayaln", cur.data)
            cur=cur.next
            cur_index+=1
        cur.next=cur.next.next
                
          
            
    


linked = Linked_list()
linked.append(12)
linked.append(2)
linked.append(1)
linked.append(5)
linked.append(14)
linked.display()
linked.delete(14)
linked.display()
# print(linked.get(1))
