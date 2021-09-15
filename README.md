# Hale-Capital
Building a trade bot through the Alpaca API. Want it to be abstract enough to implement
various strategies relatively easily. Will begin by implementing traditional strategies,
and as this process matures, would like to begin implementing reinforcement learning
models in lieu of strategies.

A back-end *may* need to be stood up at some point in the future. Will need to evaluate
what Alpaca stores versus what we need.

The bot will be deployed to GCP Google Kubernetes Engine (GKE).




### Trader Object
Interfaces with the brokerage object. It is what executes the actions, as
well as contains the watchlist of stock and stock data from Alpaca.

### Market Object
Contains all relevant state data for the agent to make an action. Pulls in data
from sources external to Alpaca, such as Twitter, Reddit, and Yahoo Finance.

### Brokerage Object
Interface for a **Trader** to interact with Alpaca.

### Position_Data Object
Data object for holding all data relevant to specific position.

## How to add a Strategy
Add your strategy in the "strategies" folder as a .py file. As parameters
it should take a Trader object, and a Market object.

Some design decisions:
- What frequency do you want to make trades?
- How do you want to determine trade quantitites?
- What features do you want to look at?
- 
