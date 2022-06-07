FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY . ${LAMBDA_TASK_ROOT}

RUN mkdir /tmp/outputs/

RUN yum -y install git
RUN yum -y install tar
RUN curl -O https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
RUN tar -zxvf openjdk-11.0.2_linux-x64_bin.tar.gz
RUN rm openjdk-11.0.2_linux-x64_bin.tar.gz
RUN mv jdk-11.0.2/ /usr/local/
ENV JAVA_HOME=/usr/local/jdk-11.0.2
ENV PATH=$PATH:$JAVA_HOME/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$JAVA_HOME/bin

# Install the function's dependencies using file requirements.txt
# from your project folder.

RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]