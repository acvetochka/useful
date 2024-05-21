# Docker

## Container management commands
| command | description |
| ------- | ------------|
| docker create image [command] | create the container |
| docker run image [command] | = create + start |
| docker rename container <new_name> | rename the container |
| docker update container | update the container config |
| docker start container ... | start the container |
| docker stop container ... | graceful* stop |
| docker kill container ... | kill (SIGKILL) the container |
| docker restart container ... | = stop + start |
| docker pause container ... | suspend the container |
| docker unpause container ... | resume the container |
| docker rm [ -f** ] container ... | destroy the container |

*send SIGTERM to the main process + SIGKILL 10 seconds later

** -f allow removing running containers (=docker kill + docker rm)
