package webserver;

import java.io.*;
import java.net.*;

public final class WebServer {
	public static void main(String[] args){
		int port = 9002;
		try {
			ServerSocket serversocket = new ServerSocket(port);
			System.out.println("Server is running...");

			while(true) {
				Socket connectionSocket = serversocket.accept();
				
				HttpRequest request = new HttpRequest(connectionSocket);
				
				Thread thread = new Thread(request);
				thread.start();
			}
		}
		catch(IOException e) {
			System.out.println(e.getMessage());
		} catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}
}
