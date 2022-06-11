import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1654631469058 = glueContext.create_dynamic_frame.from_catalog(
    database="db_yt_cleaned",
    table_name="cleaned_json_data",
    transformation_ctx="AWSGlueDataCatalog_node1654631469058",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1654631480439 = glueContext.create_dynamic_frame.from_catalog(
    database="db_yt_cleaned",
    table_name="stat_file",
    transformation_ctx="AWSGlueDataCatalog_node1654631480439",
)

# Script generated for node Join
Join_node1654631490581 = Join.apply(
    frame1=AWSGlueDataCatalog_node1654631480439,
    frame2=AWSGlueDataCatalog_node1654631469058,
    keys1=["category_id"],
    keys2=["id"],
    transformation_ctx="Join_node1654631490581",
)

# Script generated for node Select Fields
SelectFields_node1654631534410 = SelectFields.apply(
    frame=Join_node1654631490581,
    paths=[
        "video_id",
        "trending_date",
        "title",
        "channel_title",
        "category_id",
        "publish_time",
        "tags",
        "views",
        "likes",
        "dislikes",
        "comment_count",
        "thumbnail_link",
        "comments_disabled",
        "ratings_disabled",
        "video_error_or_removed",
        "description",
        "snippet_title",
        "snippet_assignable",
        "snippet_channelid",
    ],
    transformation_ctx="SelectFields_node1654631534410",
)

# Script generated for node Amazon S3
AmazonS3_node1654631578520 = glueContext.getSink(
    path="s3://proj-yt-final-bucket",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["category_id"],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1654631578520",
)
AmazonS3_node1654631578520.setCatalogInfo(
    catalogDatabase="proj_yt_analytic_db", catalogTableName="final_db"
)
AmazonS3_node1654631578520.setFormat("json")
AmazonS3_node1654631578520.writeFrame(SelectFields_node1654631534410)
job.commit()
