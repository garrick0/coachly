#docker build -t dldev .

#!/bin/bash

# Fetch the latest tag from Docker Hub using Docker Hub API or local file
latest_tag=$(<latest_tag.txt)

# Increment the tag. This example assumes the tag is a simple integer.
new_tag=$((latest_tag + 1))

# Save the new tag for future use
echo $new_tag > latest_tag.txt

# Build the new image
docker build -t garrick0/coachly:$new_tag .

# Push the new image - if needed
#docker push garrick0/coachly:$new_tag

