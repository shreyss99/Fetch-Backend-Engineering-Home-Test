# Fetch-Backend-Engineering-Home-Test

## Points Calculation

#### Background:
     
    Fetch users have points in their accounts. Users only see a single balance in their accounts. But for   reporting purposes, Fetch actually track their points per payer. In the system, each transaction record contains: payer (string), points (integer), timestamp (date). 
    For earning points, it is easy to assign a payer. Fetch know which actions earned the points. And thus, which partner should be paying for the points. 
    When a user spends points, they do nott know or care which payer the points come from. But, the accounting     team does care how the points are spent. There are two rules for determining what points to "spend" first: 
    1) We want the oldest points to be spent first (oldest based on transaction timestamp, not the order they arere received) 
    2) We want no payer's points to go negative.
