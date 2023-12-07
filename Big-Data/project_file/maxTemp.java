import java.io.IOException;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class MaxTemperature {

 public static class MaxTemperatureMapper extends Mapper<Object, Text, Text, IntWritable> {
   private final static IntWritable one = new IntWritable(1);
   private Text word = new Text();

   public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
     String[] fields = value.toString().split(",");
     String year = fields[0];
     int temperature = Integer.parseInt(fields[1]);
     context.write(new Text(year), new IntWritable(temperature));
   }
 }

 public static class MaxTemperatureReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
   public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
     int maxValue = Integer.MIN_VALUE;
     for (IntWritable val : values) {
       maxValue = Math.max(maxValue, val.get());
     }
     context.write(key, new IntWritable(maxValue));
   }
 }

 public static void main(String[] args) throws Exception {
   Configuration conf = new Configuration();
   String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
   if (otherArgs.length != 2) {
     System.err.println("Usage: MaxTemperature <in> <out>");
     System.exit(2);
   }
   Job job = Job.getInstance(conf, "Max Temperature");
   job.setJarByClass(MaxTemperature.class);
   job.setMapperClass(MaxTemperatureMapper.class);
   job.setCombinerClass(MaxTemperatureReducer.class);
   job.setReducerClass(MaxTemperatureReducer.class);
   job.setOutputKeyClass(Text.class);
   job.setOutputValueClass(IntWritable.class);
   FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
   FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
   System.exit(job.waitForCompletion(true) ? 0 : 1);
 }
}

/*
import java.io.*;
import java.util.*;

public class MaxTemperature {
  public static void main(String[] args) throws IOException {
      File file = new File("weatherdata.txt");
      Scanner scanner = new Scanner(file);
      Map<String, Integer> maxTemperature = new HashMap<>();

      while (scanner.hasNext()) {
          String[] fields = scanner.nextLine().split(",");
          String year = fields[0];
          int temperature = Integer.parseInt(fields[1]);
          maxTemperature.put(year, Math.max(maxTemperature.getOrDefault(year, Integer.MIN_VALUE), temperature));
      }

      for (Map.Entry<String, Integer> entry : maxTemperature.entrySet()) {
          System.out.println("Year: " + entry.getKey() + ", Max Temperature: " + entry.getValue());
      }
  }
}

 */