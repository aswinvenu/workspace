#include <stdio.h>

static unsigned int collatz(unsigned int num)
{
	if((num % 2) == 0){
		//printf("%d,",num/2);
		return (num/2);
	}else{
		//printf("%d,",(3*num)+1);
		return ((3*num)+1);
	}
}

int main(void)
{
	/* Opening a file to store the results */
	FILE *fp;
	unsigned long num,n,ret_num=0,count=0,max=0;
	
	/* Opening the file */
	
	fp = fopen("/home/aswin/collatz_1.csv","wb");
	for(n = 2; n < 10000; n = n+1){
	num = n;
	do{
		ret_num = collatz(num);
		count++;
		num = ret_num;
	}while(ret_num > 1);		
	
	/* checking the maximum is this num or not */
	if(count > max){
		max = count;
	}

	/* printing the result */
	printf("\n%lu : Number of iteration : %lu",n,count);
	fprintf(fp,"%lu %lu\r\n",n,count);
	count = 0;
	}
	
	/* printing the maximum number of iteration occured */
	printf(" The maximum number of iteration registered is : %lu",max);
	/* Close the file */
	fclose(fp);
	return 0;
}
