FROM alpine:latest

# Install clang and make for compilation step
RUN apk add --no-cache clang make

# Create unprivileged user (but kinda not really for now)
RUN adduser -D -u 1000 sandbox

USER sandbox

ENTRYPOINT ["/speller/docker_entry.sh"]