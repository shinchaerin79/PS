package lv1.p2588;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int a = sc.nextInt();
    int b = sc.nextInt();

    int b1 = b % 10;   
    int b10 = (b / 10) % 10;
    int b100 = b / 100;

    System.out.println(a * b1);
    System.out.println(a * b10);
    System.out.println(a * b100);

    System.out.println(a*b);

    sc.close();
  }  
}
