input = """160
34
123
159
148
93
165
56
179
103
171
44
110
170
147
98
25
37
137
71
5
6
121
28
19
134
18
7
66
90
88
181
89
41
156
46
8
61
124
9
161
72
13
172
111
59
105
51
109
27
152
117
52
68
95
164
116
75
78
180
81
47
104
12
133
175
16
149
135
99
112
38
67
53
153
2
136
113
17
145
106
31
45
169
146
168
26
36
118
62
65
142
130
1
140
84
94
141
122
22
48
102
60
178
127
73
74
87
182
35"""

inputs = [int(i) for i in input.split("\n")]
inputs.append(0)
inputs.sort()
inputs.append(inputs[-1] + 3)

"""one"""
differences = [0, 0, 0, 0]
for i in range (1, len(inputs)):
    differences[inputs[i] - inputs[i-1]] += 1
print(differences[1] * differences[3])

"""two"""
graph = []
class Node:
    def __init__(self, id):
        self.id = id
        self.edges = []
        
    def add_edge(self, node):
        self.edges.append(node)

for i in inputs:
    graph.append(Node(i))

for i in range(0, len(inputs)):
    for j in range(1, 4):
        try:
            if inputs[i+j] in range(inputs[i] + 1, inputs[i] + 4):
                graph[i].add_edge(graph[i+j])
        except:
            continue

"""will give correct solution in approx 2 weeks"""
num_paths = 0
def breadth_first_count(source_node, destination_node):
    global num_paths
    if source_node is destination_node:
        num_paths += 1
    else:
        for e in source_node.edges:
            breadth_first_count(e, destination_node)

breadth_first_count(graph[0], graph[-1])
print(num_paths)
