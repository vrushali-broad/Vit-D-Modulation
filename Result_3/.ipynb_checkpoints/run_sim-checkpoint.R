library(BoolNet)

# Function to log a message with a timestamp
logMessage <- function(message) {
  timestamp <- format(Sys.time(), "%Y-%m-%d %H:%M:%S")
  message(paste0("[", timestamp, "] ", message))
}

logMessage("Starting simulation")

## VitD = 0
logMessage("Loading network for VitD = 0")
network = loadNetwork('Rules/VitD_0_rules.txt')
logMessage("Generating time series for VitD = 0")
series = generateTimeSeries(network,100,800,type = "asynchronous",noiseLevel = 0)
write.table(series, "Output/output_VitD_0.txt", sep="\t")
logMessage("Time series for VitD = 0 completed")

## PMCA = 0
logMessage("Loading network for VitD = 1, PMCA = 0")
network = loadNetwork('Rules/VitD_1_PMCA_0_rules.txt')
logMessage("Generating time series for VitD = 1, PMCA = 0")
series = generateTimeSeries(network,100,800,type = "asynchronous",noiseLevel = 0)
write.table(series, "Output/output_VitD_1_PMCA_0.txt", sep="\t")
logMessage("Time series for VitD = 1, PMCA = 0 completed")

## PMCA = 1
logMessage("Loading network for VitD = 1, PMCA = 1")
network = loadNetwork('Rules/VitD_1_PMCA_1_rules.txt')
logMessage("Generating time series for VitD = 1, PMCA = 1")
series = generateTimeSeries(network,100,800,type = "asynchronous",noiseLevel = 0)
write.table(series, "Output/output_VitD_1_PMCA_1.txt", sep="\t")
logMessage("Time series for VitD = 1, PMCA = 1 completed")

## CYP24A1, PMCA = 0
logMessage("Loading network for VitD = 1, PMCA = 0, CYP24A1")
network = loadNetwork('Rules/VitD_1_CYP24A1_1_rules.txt')
logMessage("Generating time series for VitD = 1, CYP24A1 = 1")
series = generateTimeSeries(network,100,800,type = "asynchronous",noiseLevel = 0)
write.table(series, "Output/output_VitD_1_CYP24A1_1.txt", sep="\t")
logMessage("Time series for VitD = 1, PMCA = 0, CYP24A1 completed")

logMessage("Simulation completed")
