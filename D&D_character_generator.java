package com.example.dddcharacterscinece;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class HelloApplication extends Application {
   @Override
   public void start(Stage stage) throws IOException {
       FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
       Scene scene = new Scene(fxmlLoader.load(), 320, 240);
       stage.setTitle("Hello!");
       stage.setScene(scene);
       stage.show();
   }
   public static void main(String[] args) {
       /*Jeremiah Tanner P.4 09/30/2022
       First I made a Scanner to get users input
       Then I made a line statement so user can see the string I typed
       Then I made a string called name to get users input.*/
       Scanner jt = new Scanner(System.in);
       System.out.println("Type First Character name: ");
       String name = jt.next();
       /*Before user sees the stat I made java create a system to print out a whole number stat randomly
       generated that goes all the way to the number 18.*/
       int STR = (int)(Math.random()*19);
       int INT = (int)(Math.random()*19);
       int WIS = (int)(Math.random()*19);
       int CON = (int)(Math.random()*19);
       int DEX = (int)(Math.random()*19);
       int CHR = (int)(Math.random()*19);
       //Then I have java output your name and print out the stats that you will see in the console.
       System.out.println(name + " your stats are:");
       System.out.println("STR: "+STR);
       System.out.println("INT: "+INT);
       System.out.println("WIS: "+WIS);
       System.out.println("CON: "+CON);
       System.out.println("DEX: "+DEX);
       System.out.println("CHR: "+CHR);
       //After that I have user input second characters name under the statement I printed to console.
       System.out.println("Type Second character name below: ");
       String nxtName = jt.next();
       /*Before user sees the stat I made java create a system to print out a whole number stat randomly
       generated that goes all the way to the number 18.*/
       int str = (int)(Math.random()*19);
       int inte = (int)(Math.random()*19);
       int wis = (int)(Math.random()*19);
       int con = (int)(Math.random()*19);
       int dex = (int)(Math.random()*19);
       int chr = (int)(Math.random()*19);
       //Then I have java output your name and print out the stats that you will see in the console.
       System.out.println(nxtName+ " your stats are:");
       System.out.println("STR: "+str);
       System.out.println("INT: "+inte);
       System.out.println("WIS: "+wis);
       System.out.println("CON: "+con);
       System.out.println("DEX: "+dex);
       System.out.println("CHR: "+chr);

       System.out.println("Type Third character name below:");
       String thrdName = jt.next();

       int stre = (int)(Math.random()*19);
       int inter = (int)(Math.random()*19);
       int wise = (int)(Math.random()*19);
       int cone = (int)(Math.random()*19);
       int dexe = (int)(Math.random()*19);
       int chre = (int)(Math.random()*19);

       System.out.println(thrdName+ " your stats are: ");
       System.out.println("STR: "+stre);
       System.out.println("INT: "+inter);
       System.out.println("WIS: "+wise);
       System.out.println("CON: "+cone);
       System.out.println("DEX: "+dexe);
       System.out.println("CHR: "+chre);
       //This then lets the user know the reroll system I will implement
       System.out.println("You only will have 1 REROLL. If REROLL wanted pick which character you want to REROLL");
       System.out.println("by number. TYPE BELOW TO REROLL!");
       // The string reroll will have input enter which character they want rerolled.
       String reroll = jt.next();

       int restr = (int)(Math.random()*19);
       int reint = (int)(Math.random()*19);
       int rewis = (int)(Math.random()*19);
       int recon = (int)(Math.random()*19);
       int redex = (int)(Math.random()*19);
       int rechr = (int)(Math.random()*19);

       /*Once user types in which character I then put an if statement that has the reroll variable equals what
       number the user inputs.*/
       if(reroll.equals("1")){
           System.out.println(name+" your new stats are: ");
           System.out.println("STR: "+restr);
           System.out.println("INT: "+reint);
           System.out.println("WIS: "+rewis);
           System.out.println("CON: "+recon);
           System.out.println("DEX: "+redex);
           System.out.println("CHR: "+rechr);
           System.out.println("Nice reroll! your characters have been saved. Please continue into the game.");
       }
       else if(reroll.equals("3")){
           System.out.println(thrdName+" your new stats are: ");
           System.out.println("STR: "+restr);
           System.out.println("INT: "+reint);
           System.out.println("WIS: "+rewis);
           System.out.println("CON: "+recon);
           System.out.println("DEX: "+redex);
           System.out.println("CHR: "+rechr);
           System.out.println("Nice reroll! your characters have been saved. Please continue into the game.");
       }
       else if(reroll.equals("2")){
           System.out.println(nxtName+" your new stats are: ");
           System.out.println("STR: "+restr);
           System.out.println("INT: "+reint);
           System.out.println("WIS: "+rewis);
           System.out.println("CON: "+recon);
           System.out.println("DEX: "+redex);
           System.out.println("CHR: "+rechr);
           System.out.println("Nice reroll! your characters have been saved. Please continue into the game.");
       }
       else{
           System.out.println("Your characters have been saved. Please continue into the game.");
       }
       //Then I added a filewriter so that the user could see the save characters in a file.
       try {
           FileWriter sheetWriter = new FileWriter("Character.txt");
           sheetWriter.write("Your first character: " + name);
           sheetWriter.write(" stats were-");
           sheetWriter.write("\nSTR: "+STR);
           sheetWriter.write("\nINT: "+INT);
           sheetWriter.write("\nWIS: "+WIS);
           sheetWriter.write("\nCON: "+CON);
           sheetWriter.write("\nDEX: "+DEX);
           sheetWriter.write("\nCHR: "+CHR);

           sheetWriter.write("\nYour second character: " + nxtName);
           sheetWriter.write(" stats were-");
           sheetWriter.write("\nSTR: "+str);
           sheetWriter.write("\nINT: "+inte);
           sheetWriter.write("\nWIS: "+wis);
           sheetWriter.write("\nCON: "+con);
           sheetWriter.write("\nDEX: "+dex);
           sheetWriter.write("\nCHR: "+chr);

           sheetWriter.write("\nYour third character: " + thrdName);
           sheetWriter.write(" stats were-");
           sheetWriter.write("\nSTR: "+stre);
           sheetWriter.write("\nINT: "+inter);
           sheetWriter.write("\nWIS: "+wise);
           sheetWriter.write("\nCON: "+cone);
           sheetWriter.write("\nDEX: "+dexe);
           sheetWriter.write("\nCHR: "+chre);



           sheetWriter.close();
           System.out.println("Check the file");
           //If something unexpected happen the file will catch it and print out "Something went wrong."
       } catch (IOException e){
           System.out.println("Something went wrong.");
           e.printStackTrace();
       }
   }
}

