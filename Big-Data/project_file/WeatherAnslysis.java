import java.io.IOException;
import java.util.Iterator;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;
import org.apache.hadoop.mapred.TextInputFormat;
import org.apache.hadoop.mapred.TextOutputFormat;

public class WeatherData {

   public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable> {
       private final static IntWritable one = new IntWritable(1);
       private Text word = new Text();

       public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
           String line = value.toString();
           String[] parts = line.split(",");
           String date = parts[0];
           int temperature = Integer.parseInt(parts[1]);
           output.collect(new Text(date), new IntWritable(temperature));
       }
   }

   public static class Reduce extends MapReduceBase implements Reducer<Text, IntWritable, Text, Text> {
       public void reduce(Text key, Iterator<IntWritable> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
           int sum = 0;
           int count = 0;
           while (values.hasNext()) {
               sum += values.next().get();
               count++;
           }
           int average = sum / count;
           if (average > 70) {
               output.collect(key, new Text("shiny"));
           } else {
               output.collect(key, new Text("cool"));
           }
       }
   }

   public static void main(String[] args) throws Exception {
       JobConf conf = new JobConf(WeatherData.class);
       conf.setJobName("weather data analysis");

       conf.setOutputKeyClass(Text.class);
       conf.setOutputValueClass(Text.class);

       conf.setMapperClass(Map.class);
       conf.setCombinerClass(Reduce.class);
       conf.setReducerClass(Reduce.class);

       conf.setInputFormat(TextInputFormat.class);
       conf.setOutputFormat(TextOutputFormat.class);

       FileInputFormat.setInputPaths(conf, new Path(args[0]));
       FileOutputFormat.setOutputPath(conf, new Path(args[1]));

       JobClient.runJob(conf);
   }
}

/*
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class WeatherData {
   public static void main(String[] args) {
       try (BufferedReader br = new BufferedReader(new FileReader("weather.csv"))) {
           String line;
           while ((line = br.readLine()) != null) {
               String[] parts = line.split(",");
               String date = parts[0];
               int temperature = Integer.parseInt(parts[1]);
               String dayType = temperature > 70 ? "shiny" : "cool";
               System.out.println(date + ": " + dayType);
           }
       } catch (IOException e) {
           e.printStackTrace();
       }
   }
}

 */