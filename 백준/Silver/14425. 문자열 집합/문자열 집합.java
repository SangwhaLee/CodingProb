import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s= br.readLine();
		StringTokenizer st = new StringTokenizer(s);
		HashMap<String, Integer> map = new HashMap<>();
		int answer=0;
		
		int N= Integer.parseInt(st.nextToken());
		int M= Integer.parseInt(st.nextToken());
		
		for(int i=0;i<N;i++) {
			String tmp = br.readLine();
			map.put(tmp, 1);
		}
		
		for(int i=0;i<M;i++) {
			String tmp = br.readLine();
			if(map.containsKey(tmp)) {
				answer++;
			}
		}
		
		System.out.println(answer);
	}

}
