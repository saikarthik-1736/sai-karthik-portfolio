# Student Marks and Grade Calculator

## 1. Aim
To write a Python program to calculate a student's grade based on the marks entered by the user using if, elif, and else conditional statements.

## 2. Procedure
1. Start the Python program.
2. Get the student's marks as input from the user.
3. Check whether the marks are greater than or equal to 90.
4. If true, display Grade A+.
5. Otherwise, check the remaining conditions using elif statements.
6. Assign grades according to the marks:
   - 90–100: A+
   - 80–89: A
   - 70–79: B
   - 60–69: C
   - 50–59: D
   - 35–49: E
   - Below 35: Fail
7. Display the corresponding grade and message.
8. Stop the program.

## 3. Flowchart

```mermaid
flowchart TD
    A[START] --> B[Enter Marks]
    B --> C{Marks >= 90?}
    C -- Yes --> D[Grade A+]
    C -- No --> E{Marks >= 80?}
    E -- Yes --> F[Grade A]
    E -- No --> G{Marks >= 70?}
    G -- Yes --> H[Grade B]
    G -- No --> I{Marks >= 60?}
    I -- Yes --> J[Grade C]
    I -- No --> K{Marks >= 50?}
    K -- Yes --> L[Grade D]
    K -- No --> M{Marks >= 35?}
    M -- Yes --> N[Grade E]
    M -- No --> O[Fail]
    D --> P[STOP]
    F --> P
    H --> P
    J --> P
    L --> P
    N --> P
    O --> P