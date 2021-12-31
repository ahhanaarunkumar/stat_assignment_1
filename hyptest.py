import math
import pandas as pd

def hyp(sample_mean, std, sample_size,population_mean, CI):
    sample_mean = sample_mean
    std = std
    sample_size = sample_size
    CI = CI
    population_mean= population_mean
    if(sample_size < 30):
            t_table = {
                # alpha values : [50, 90, 95, 99]
                1: {50: 1.000, 90: 6.314, 95: 12.706, 99: 63.657},
                2: {50: 0.816, 90: 2.920, 95: 4.303, 99: 9.925},
                3: {50: 0.765, 90: 2.353, 95: 3.182, 99: 5.841},
                4: {50: 0.741, 90: 2.132, 95: 2.770, 99: 4.604},
                5: {50: 0.727, 90: 2.015, 95: 2.571, 99: 4.032},
                6: {50: 0.718, 90: 1.943, 95: 2.447, 99: 3.707},
                7: {50: 0.711, 90: 1.895, 95: 2.365, 99: 3.499},
                8: {50: 0.706, 90: 1.860, 95: 2.306, 99: 3.355},
                9: {50: 0.703, 90: 1.833, 95: 2.262, 99: 3.250},
                10: {50: 0.700, 90: 1.812, 95: 2.228, 99: 3.169},
                11: {50: 0.697, 90: 1.796, 95: 2.201, 99: 3.106},
                12: {50: 0.695, 90: 1.782, 95: 2.179, 99: 3.055},
                13: {50: 0.694, 90: 1.771, 95: 2.160, 99: 3.012},
                14: {50: 0.692, 90: 1.761, 95: 2.145, 99: 2.977},
                15: {50: 0.691, 90: 1.753, 95: 2.131, 99: 2.947},
                16: {50: 0.690, 90: 1.746, 95: 2.120, 99: 2.921},
                17: {50: 0.689, 90: 1.740, 95: 2.110, 99: 2.898},
                18: {50: 0.688, 90: 1.734, 95: 2.101, 99: 2.878},
                19: {50: 0.688, 90: 1.729, 95: 2.093, 99: 2.861},
                20: {50: 0.687, 90: 1.725, 95: 2.086, 99: 2.845},
                21: {50: 0.686, 90: 1.721, 95: 2.080, 99: 2.831},
                22: {50: 0.686, 90: 1.717, 95: 2.074, 99: 2.819},
                23: {50: 0.685, 90: 1.714, 95: 2.069, 99: 2.807},
                24: {50: 0.685, 90: 1.711, 95: 2.064, 99: 2.797},
                25: {50: 0.684, 90: 1.708, 95: 2.060, 99: 2.787},
                26: {50: 0.684, 90: 1.706, 95: 2.056, 99: 2.779},
                27: {50: 0.684, 90: 1.703, 95: 2.052, 99: 2.771},
                28: {50: 0.683, 90: 1.701, 95: 2.048, 99: 2.763},
                29: {50: 0.683, 90: 1.699, 95: 2.045, 99: 2.756},

            }

            try:
                deg_freedom = sample_size - 1
                t_alpha = t_table[deg_freedom][CI]

                t_stat = (sample_mean-population_mean)/(std/math.sqrt(sample_size))

                if(abs(t_stat) > t_alpha):
                    print("Data follows the t-distribution and Null Hypothesis rejected")
                else:
                    print("Data follows the t-distribution and Null Hypothesis accepted")
            except Exception as e:
                print(e)
    else:
            # z-distribution
            alpha_by_two = (100-CI)/(2*100)
            # 90,95,98,99
            try:
                z_scores = {0.05: 1.64, 0.025: 1.96, 0.01: 2.33, 0.005: 2.575}
                z = z_scores[alpha_by_two]

                z_stat = (sample_mean-population_mean)/(std/math.sqrt(sample_size))

                if(abs(z_stat) > z):
                    print("Data follows the z-distribution and Null Hypothesis rejected")
                else:
                    print("Data follows the z-distribution and Null Hypothesis accepted")
                
            except Exception as e:
                print(e)



def main(csv,sample_mean, std, population_mean, sample_size,CI):
    csv = csv
    sample_mean = sample_mean
    std = std
    population_mean = population_mean
    sample_size = sample_size
    CI = CI
    if(csv):
        df = pd.read_csv(csv)
        col_name = input("Enter the column name:")
        sample_mean = df[col_name].mean()
        std = df[col_name].std()
        sample_size = df[col_name].count()
        hyp(sample_mean, std, sample_size,population_mean,CI)
        
    else:
       hyp(sample_mean, std, sample_size,population_mean,CI)

     
main(0,6.1,0.2,6,30,95)