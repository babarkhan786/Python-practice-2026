# My First Markdown File

This is **bold** text.

This is *italic* text.

## List

- Python
- NumPy
- Pandas

## Code

```python
print("Hello, World!")
```
# Markdown Graphs Using Mermaid

This document demonstrates how to create graphs in Markdown using Mermaid.

---

# 1. Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Read Data]
    B --> C[Process Data]
    C --> D[Generate Results]
    D --> E[End]
```

---

# 2. Left-to-Right Flowchart

```mermaid
flowchart LR
    A[Python] --> B[NumPy]
    B --> C[Pandas]
    C --> D[Matplotlib]
```

---

# 3. Decision Tree

```mermaid
flowchart TD
    A{Temperature > 30?}
    A -- Yes --> B[Turn ON Fan]
    A -- No --> C[Turn OFF Fan]
```

---

# 4. Sequence Diagram

```mermaid
sequenceDiagram
    User->>Python: Run Script
    Python->>File: Read Data
    File-->>Python: Return Data
    Python-->>User: Display Output
```

---

# 5. Class Diagram

```mermaid
classDiagram
    class Student{
        +String name
        +int age
        +study()
    }

    class Teacher{
        +teach()
    }

    Student --> Teacher
```

---

# 6. State Diagram

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Running
    Running --> Finished
    Finished --> [*]
```

---

# 7. Pie Chart

```mermaid
pie title Student Marks
    "Python" : 35
    "NumPy" : 25
    "Pandas" : 20
    "Matplotlib" : 20
```

---

# 8. Git Graph

```mermaid
gitGraph
    commit
    branch feature
    checkout feature
    commit
    commit
    checkout main
    merge feature
```

---

# 9. Entity Relationship Diagram

```mermaid
erDiagram
    STUDENT ||--o{ COURSE : enrolls
    COURSE ||--o{ TEACHER : taught_by
```

---

# 10. Gantt Chart

```mermaid
gantt
    title Python Learning Plan

    dateFormat YYYY-MM-DD

    section Basics
    Variables :done, a1, 2026-08-01,3d
    Loops :done, a2, after a1,2d

    section Libraries
    NumPy :a3, after a2,4d
    Pandas :a4, after a3,4d
```

---

# 11. Mind Map

```mermaid
mindmap
  root((Python))
    Basics
      Variables
      Loops
      Functions
    Libraries
      NumPy
      Pandas
      Matplotlib
```

---

# 12. Journey Diagram

```mermaid
journey
    title Learning Python
    section Beginner
      Install Python: 5: Student
      Learn Variables: 4: Student
    section Intermediate
      Learn NumPy: 3: Student
      Learn Pandas: 4: Student
```
1. Mermaid (Most Popular)
Flowchart
```mermaid
flowchart TD
A --> B
B --> C
```
Graph
```mermaid
graph LR
A --> B
B --> C
C --> D
```
Sequence Diagram
```mermaid
sequenceDiagram
Alice->>Bob: Hello
Bob-->>Alice: Hi
```
Class Diagram
```mermaid
classDiagram
Animal <|-- Dog
Animal <|-- Cat
```
State Diagram
```mermaid
stateDiagram-v2
[*] --> Idle
Idle --> Running
Running --> [*]
```
Pie Chart
```mermaid
pie
title Fruit Sales
"Apple" : 40
"Orange" : 30
"Banana" : 30
```
Gantt Chart
```mermaid
gantt
title Project Schedule
dateFormat YYYY-MM-DD

section Coding
Python :2026-08-01,5d

section Testing
Debug :2026-08-06,3d
```
Mind Map
```mermaid
mindmap
root((Python))
    Basics
        Variables
        Loops
    Libraries
        NumPy
        Pandas
```
Entity Relationship Diagram
```mermaid
erDiagram
STUDENT ||--o{ COURSE : enrolls
```
Git Graph
```mermaid
gitGraph
commit
branch feature
checkout feature
commit
checkout main
merge feature
```
2. Graphviz (DOT)

Many Markdown editors support Graphviz.

```dot
digraph G {
    A -> B;
    B -> C;
    C -> D;
}
```
3. PlantUML
```plantuml
@startuml
Alice -> Bob: Hello
Bob --> Alice: Hi
@enduml
```
4. D2
```d2
A -> B
B -> C
C -> D
```
5. Vega-Lite (Data Charts)

Some Markdown systems (such as Jupyter Book and Observable) support Vega-Lite for charts.

```vega-lite
{
  "mark": "bar",
  "encoding": {
    "x": {"field": "Name", "type": "nominal"},
    "y": {"field": "Value", "type": "quantitative"}
  },
  "data": {
    "values": [
      {"Name":"A","Value":5},
      {"Name":"B","Value":10}
    ]
  }
}
```