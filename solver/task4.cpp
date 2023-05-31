#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char *argv[]) {
    double R1, R2, R3, R_sum,
        Es_R1, Es_R2, Es_R3, Es_R_sum,
        Ei_R1, Ei_R2, Ei_R3, Ei_R_sum;

    double R23, R4;
    double TR1, TR2, TR3, TR4, TR_sum;
    double EmR1, EmR2, EmR3, EmR4, EmR_sum;
    double delta2, delta3;
    double EsR4, EiR4;
    double R4_max, R4_min;


    if (argc < 12 + 1) {
      cout << "12 args";
      return -1;
    }
    R1 = stod(argv[1]);
    R2 = stod(argv[2]);
    R3 = stod(argv[3]);
    R_sum = stod(argv[4]);
    Es_R1 = stod(argv[5]);
    Es_R2 = stod(argv[6]);
    Es_R3 = stod(argv[7]);
    Es_R_sum = stod(argv[8]);
    Ei_R1 = stod(argv[9]);
    Ei_R2 = stod(argv[10]);
    Ei_R3 = stod(argv[11]);
    Ei_R_sum = stod(argv[12]);

    R23 = (R2 * R3) / (R2 + R3);
    R4 = R_sum - R1 - R23;

    TR1 = Es_R1 - Ei_R1;
    TR2 = Es_R2 - Ei_R2;
    TR3 = Es_R3 - Ei_R3;
    TR_sum = Es_R_sum - Ei_R_sum;

    EmR1 = (Es_R1 + Ei_R1) / 2;
    EmR2 = (Es_R2 + Ei_R2) / 2;
    EmR3 = (Es_R3 + Ei_R3) / 2;
    EmR_sum = (Es_R_sum + Ei_R_sum) / 2;

    delta2 = pow(R3,2) / pow(R2 + R3,2);
    delta3 = pow(R2, 2) / pow(R2 + R3, 2);

    TR4 = TR1 + delta2 * TR2 + delta3 * TR3 - TR_sum;
    EmR4 = EmR_sum - EmR1 - delta2 * EmR2 - delta3 * EmR3;

    EsR4 = EmR4 + TR4 / 2;
    EiR4 = EmR4 - TR4 / 2;

    R4_max = R4 + EsR4;
    R4_min = R4 + EiR4;

    cout << R4_max << " " << R4_min;

    return 0;
}
