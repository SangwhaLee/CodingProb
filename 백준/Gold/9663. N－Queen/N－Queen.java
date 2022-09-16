import java.util.*;
import java.io.*;

public class Main {
	static int[] arr;
	static int count=0;
	static int num;
	
	static void Queen(int depth) {
		if(depth == num) {
			count++;
			return;
		}
		
		for(int i=0;i<num;i++) {
			arr[depth]=i;
			
			if(Possibility(depth)) {
				Queen(depth+1);
			}
		}
	}
	
	static boolean Possibility(int col) {
		for(int i=0;i<col;i++) {
			if(arr[col]==arr[i]) {
				return false;
			}
			
			else if(Math.abs(col-i) == Math.abs(arr[col]-arr[i])) {
				return false;
			}
		}
		
		return true;
	}

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		num = N;
		arr = new int[num];
		
		Queen(0);
		
		System.out.println(count);
	}

}