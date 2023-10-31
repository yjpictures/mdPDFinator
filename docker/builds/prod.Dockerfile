# base image
FROM ubuntu:22.04

LABEL org.opencontainers.image.authors="hello@yashj.ca"

# update and upgrade the packages
RUN apt update && \
    apt upgrade -y

# install weasyprint dependencies
RUN apt install -y \
        python3-dev \
        python3-pip \
        python3-cffi \
        libcairo2 \
        libpango1.0-0 \
        libgdk-pixbuf2.0-0 \
        libffi-dev \
        shared-mime-info

# copy the binary
COPY dist/mdPDFinator /usr/local/src/

# create the binary execuatable
RUN chmod 775 /usr/local/src/mdPDFinator

# add the binary to path
ENV PATH="${PATH}:/usr/local/src/"

# add local folder to app
VOLUME ["/app"]
WORKDIR /app

# create mdPDFinator entrypoint
ENTRYPOINT ["mdPDFinator"]
