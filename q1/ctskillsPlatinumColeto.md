# Computational Thinking Exercise
## Smart School Canteen Queue
**Name:** Alexander Mari Coleto
**Section:** 9-Platinum
**Last Name:** Coleto
**Date:** Date Completed
---

## Step 1: Identify the Big Problem
### Main Problem
The PSHS school canteen often gets crowded due to inefficiency, especially at lunch. Root causes include unorganized systems, line cutting, and having more than 1 receipt.
## Step 2: Identify the Sub-Problems
1. Students take too long to order: no organized way to view every price of goods before reaching the cashier. Students also ask prices to the cashier, which takes a valuable amount of time away from efficiency.
2. Students could cut lines or have more than 1 receipt.
3. The canteen has no system for tracking the quantity of goods. Cashiers ask those who serve, which takes up valuable time. Additionally, when the goods are already sold out but people have put it in their receipt, they get it refunded from the cashier, which also takes away time.
4. Students may not know when their order is finished, which may lead to mix ups. Thus, taking up more time. 

---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem                                            | CT Skill                                  | Proposed Solution                               |
|--------------------------------------------------------|-------------------------------------------|-------------------------------------------------|
| No Organized System to view price of goods             | Abstraction                               | Digital searchable price list in a QR code/app  |
| Students cutting lines or have more than 1 receipt     | Algorithmic Design                        | Numbered ticket system                          |
| No system to track quantity of goods left              | Abstraction, Problem Decomposition        | Inventory list that updates each order          |
| Students not knowing when their order is finished      | Algorithmic Design, Problem Decomposition | Install a display screen                        |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Sub-problem 3: No system to track quantity of goods left.
### Pseudocode
START

    INITIALIZE netquantityitems = stockamount 
    INITIALIZE canteen = open

    WHILE CANTEEN is OPEN
        IF student_orders THEN
            IF netquantityitems > 0 THEN
                PROCEED
                netquantityitems = netquantityitems - 1
                PRINT receipt_with_nummber
            
            ELSE
                SHOW "Item Sold Out"
                DISCARD itemorder
        ENDIF
    ENDWHILE
END