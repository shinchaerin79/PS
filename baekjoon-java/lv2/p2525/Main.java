package lv2.p2525;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int A = sc.nextInt();
    int B = sc.nextInt();
    int C = sc.nextInt();

    int newHour = A;
    int newMin = B + C;

    if (newMin < 60) {
      System.out.printf("%d %d", newHour, newMin);
    } else if (newMin >= 60) {
      newHour += newMin / 60;
      newMin = newMin % 60;

      if (newHour < 24) {
        System.out.printf("%d %d", newHour, newMin);
      } else {
        System.out.printf("%d %d", newHour - 24, newMin);
      }
    }
    sc.close();
  }
}
