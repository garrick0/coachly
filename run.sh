#VERSION=5
VERSION=$(<latest_tag.txt)
docker pull garrick0/coachly:$VERSION
docker run --name coachly -it --rm -p 80:80 garrick0/coachly:$VERSION
