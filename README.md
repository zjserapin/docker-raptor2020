# docker-raptor2020

This app is for UNC Charlotte DSBA 6190 Class in Spring 2020.  We were asked to do the following items for the assignment.

1) Create a customized Docker container from the current version of Python that deploys a simple python script.
2) Push the image to DockerHub
3) Pull the Image down and run it on a cloud platform cloud shell: Google Cloud Shell or AWS Cloud9.

I created a simple random choice app that randomly selects 2 teams from the 2020 all_star starters.  Then using 538's raptor ratings, a pythagrian sum is generated to give a win probability for the team most likley to win.
Sources: https://projects.fivethirtyeight.com/2020-nba-player-ratings/, https://projects.raspberrypi.org/en/projects/team-chooser/4