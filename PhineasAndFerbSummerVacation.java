import java.util.Scanner;

public class PhineasAndFerbSummerVacation {
  public static void main(String[] args) {
    // Ask the user what they did for summer vacation
    System.out.println("What did you do for summer vacation?");
    Scanner scanner = new Scanner(System.in);
    String userResponse = scanner.nextLine();

    // Initialize an array of programmed responses
    String[] programmedResponses = {
      "I built a rocket ship to the moon.",
      "I created a time machine.",
      "I built a robot to do my homework.",
      "I invented a machine that turns objects into gold.",
      "I travelled to the future and back.",
      "I went on a wild adventure with Agent P.",
      "I spent the summer at the beach, building sandcastles and surfing waves.",
      "I learned how to play the guitar and wrote my own songs.",
      "I started my own business selling handmade crafts.",
      "I volunteered at a local animal shelter and helped care for the animals."
    };

    // Use a loop to go through each programmed response and check if it contains the user's response
    for (String response : programmedResponses) {
      if (response.toLowerCase().contains(userResponse.toLowerCase())) {
        // If the user's response is contained in the programmed response, print it out
        System.out.println(response);
        // Exit the loop
        break;
      }
    }

    // If the user's response was not contained in any of the programmed responses, print out a default response
    System.out.println("That sounds like a really fun summer vacation! I hope you had a great time.");
  }
}
