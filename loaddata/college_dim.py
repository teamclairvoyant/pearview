
from pyspark.sql.functions import col, count,monotonically_increasing_id
from common.read_wrapper import read_from_csv
from common.spark_utility import create_spark_session
from common.write_redshift import write_to_redshift, write_to_mysql

spark = create_spark_session()
#print(spark)
df_college=read_from_csv(spark,"../output/college/target_mapped_data_college.csv")
#df_college.show(10)
df_college_dim = df_college.select("CollegeId", "CollegeName", "UniversityId", "CollegeAddress", "City", "ZipCode")
df_college_dim.show()
write_to_mysql(df_college_dim,"college_dim")
#write_to_redshift(df_college, "college_dim")