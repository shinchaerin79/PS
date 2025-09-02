package lv2.p2884;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int H = sc.nextInt();
    int M = sc.nextInt();

    if (M >= 45) {
      System.out.printf("%d %d",H, M-45);
    } else {
      H--;
      if (H < 0) {
        H = 23;
      }
      System.out.printf("%d %d", H, 60 - (45 - M));
    }
    sc.close();
  }
}
