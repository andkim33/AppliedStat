RStandardization = function(data, method=“zscore”)
{
    if(method != “zscore”) method = “minmax”
    if(method = “zscore”)
       zdata = scale(data, center=TRUE, scale=TRUE)    
    else if(method = “minmax”)
       {
            # 0-1 transformation
            maxX = apply(data, 2, max)
            minX = apply(data, 2, min)   
            zdata = scale(data, center=minX, scale=maxX – minX)
        }
     return(zdata)
}

RStandardization_test = function(train_data, test_data,
                               method=“zscore”)
 {
  if(method != “zscore”) method = “minmax”
  if(method = “zscore”)
  {
    zX_mean = apply(train_data, 2, mean, na.rm = TRUE)     
    zX_sd = apply(train_data, 2, sd, na.rm = TRUE))
    zdata_test = scale(test_data, center=zX_mean, scale=zX_sd)
  }
 else if(method = “minmax”)
  {
   # 0-1 transformation
    maxX = apply(train_data, 2, max)
    minX = apply(train_data, 2, min)   
    zdata_test = scale(test_data, center=minX, scale=maxX - minX)
   }
    return(zdata_test)
}

data(iris)
train_test = Train_Test_Split_m1(iris, SplitRatio=0.8)
train = train_test$train_data
test = train_test$test_data
ztest = RStandardization_test(train, test, method=“minmax”)
head(ztest)

