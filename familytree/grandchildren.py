from familytree import Familytree

grandchild1 = Familytree('Darren', 'Tran', 'Male', 'Boy', 'June', 26, 2007,
                         'Lien', 'Dang', 'Minh', 'Tran', 'Yes')
grandchild2 = Familytree('Evan', 'Tran', 'Male', 'Boy', 'April', 21, 2008,
                         'Nga', 'Dang', 'Phong', 'Tran', 'Yes')

# print(grandchild1.gender)
# print(grandchild1.mother_name)
# print(grandchild1.father_name)
# print(grandchild1.is_grandkid)

# print(Familytree.name(grandchild1))
# print(Familytree.birthday(grandchild1))
# print(Familytree.mother_name(grandchild1))
# print(Familytree.father_name(grandchild1))
#
# print(Familytree.name(grandchild2))
# print(Familytree.birthday(grandchild2))
# print(Familytree.mother_name(grandchild2))
# print(Familytree.father_name(grandchild2))

# print(Familytree.name(grandchild1))
# print(grandchild1.name)

Familytree.child_info(grandchild1)