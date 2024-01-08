#getting base image(os on which java already installed)
FROM openjdk:11

#working directory on which all the code will be kept (inside container)
WORKDIR app/

#copy the app from your system to the current working directory  of container
COPY  HelloWorld.java .

#compile code
RUN javac HelloWorld.java

#run java compiled code
CMD ["java","HelloWorld"]
