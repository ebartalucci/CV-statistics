# Structure of the code

- I am using the Github API to let python interact with my Github data and to manage my repositories
- Initialize API token
- Fetch data from my account (only public repositories). For private repos I still need to find a solution
- Create a document where to list all the data of interest
- Create function to read repos-specific data for each project and store
- Create function to cathegorize readed data based on extension (e.g. .py, .m ecc)
- Create function for opening and reading out number of lines for each of the file and store
- Create function to materialize output in a .csv format and plot as pie chart
- Customize plot, filter by programming language type, number of lines as an inset
