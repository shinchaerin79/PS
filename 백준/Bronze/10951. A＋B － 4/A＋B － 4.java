import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()) {   // 더 이상 입력이 없으면 종료
            int A = sc.nextInt();
            int B = sc.nextInt();
            System.out.println(A + B);
        }

        sc.close();
    }
}
