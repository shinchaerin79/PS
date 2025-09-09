import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine()); // 테스트케이스 개수
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < T; i++) {
            String[] nums = br.readLine().split(" ");
            int A = Integer.parseInt(nums[0]);
            int B = Integer.parseInt(nums[1]);

            sb.append(A + B).append('\n');  // 한 줄에 결과 저장
        }

        System.out.print(sb); // 한 번에 출력
    }
}
