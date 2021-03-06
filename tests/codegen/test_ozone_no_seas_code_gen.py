import pandas as pd
import numpy as np

import pyaf.ForecastEngine as autof
import pyaf.Bench.TS_datasets as tsds

import pyaf.CodeGen.TS_CodeGenerator as tscodegen

#get_ipython().magic('matplotlib inline')

b1 = tsds.load_ozone()
df = b1.mPastData

#df.tail(10)
#df[:-10].tail()
#df[:-10:-1]
#df.describe()



H = b1.mHorizon;

N = df.shape[0];
for n in range(N,  N+1 , 10):
    df1 = df.head(n).copy();
    lEngine = autof.cForecastEngine()
    lEngine
    lEngine.mOptions.mEnableSeasonals = False;
    lEngine.mOptions.mDebugCycles = False;
    lEngine.mOptions.mCycle_Criterion_Threshold = 20000;
    lEngine.train(df1 , b1.mTimeVar , b1.mSignalVar, H);
    lEngine.getModelInfo();
    lEngine.mSignalDecomposition.mBestModel.mTimeInfo.mResolution
    lCodeGenerator = tscodegen.cTimeSeriesCodeGenerator();
    lSQL = lCodeGenerator.testGeneration(lEngine);
