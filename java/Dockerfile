#getting base image(os on which java already installed)
FROM

#working directory on which all the code will be kept (inside container)
WORKDIR app/

#copy the app from your system to the current working directory  of container
COPY  Hello.java .

#compile code
RUN javac Hello.java

#run java compiled code
CMD ["java","Hello"]
