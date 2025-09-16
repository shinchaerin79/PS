import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();  // N 입력 받기

        for (int i = 1; i <= N; i++) {
            // i만큼 별 출력
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();  // 줄바꿈
        }

        sc.close();
    }
}
