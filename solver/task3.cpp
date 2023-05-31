#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char *argv[])
{
    double d_max, d_min, S_max, S_min,
        EPC_max, EPC_min, D_max, D_min;

    int k = atoi(argv[1]);

    d_max = stod(argv[2]);
    d_min = stod(argv[3]);
    S_max = stod(argv[4]);
    S_min = stod(argv[5]);
    EPC_max = stod(argv[6]);
    EPC_min = stod(argv[7]);
    D_max = stod(argv[8]);
    D_min = stod(argv[9]);

    double d, D, S, EPC, L;
    double Esd, EsD, EsS, EsEPC, EsL;
    double Eid, EiD, EiS, EiEPC, EiL;
    double Td, TD, TS, TL, TEPC;
    double Emd, EmD, EmS, EmEPC, EmL;

    d = round((d_max + d_min) / 2);
    Esd = d_max - d;
    Eid = d_min - d;

    D = round((D_max + D_min) / 2);
    EsD = D_max - D;
    EiD = D_min - D;

    S = round((S_max + S_min) / 2);
    EsS = S_max - S;
    EiS = S_min - S;

    EPC = round((EPC_max + EPC_min) / 2);
    EsEPC = EPC_max - EPC;
    EiEPC = EPC_min - EPC;

    L = d / 2 + D / 2 + S - EPC;

    cout << L;
    
    if (k == 1)
    {
        EsL = EsS + Eid / 2 + EiD / 2 - EsEPC;
        EiL = EiS + Esd / 2 + EsD / 2 - EiEPC;

        Td = Esd - Eid;
        TD = EsD - EiD;
        TS = EsS - EiS;
        TEPC = EsEPC - EiEPC;
        TL = EsL - EiL;

        if (Td / 2 + TD / 2 + TL + TEPC != TS) { cout << "���-�� ����� �� ���..."; }

        EsL = EsL * 1000;
        EiL = EiL * 1000;

        cout << EsL << " " << EiL;
        return 0;
    }

    if (k == 2)
    {
        EmS = (EsS + EiS) / 2;
        Emd = (Esd + Eid) / 2;
        EmD = (EsD + EiD) / 2;
        EmEPC = (EsEPC + EiEPC) / 2;

        EmL = EmS + Emd / 2 + EmD / 2 - EmEPC;

        Td = Esd - Eid;
        TD = EsD - EiD;
        TS = EsS - EiS;
        TEPC = EsEPC - EiEPC;

        TL = sqrt(pow(TS, 2.0) - pow(TEPC, 2.0) - pow(Td / 2, 2.0) - pow(TD / 2, 2.0));

        EsL = EmL + TL / 2;
        EiL = EmL - TL / 2;

        EsL = EsL * 1000;
        EiL = EiL * 1000;

        cout << EsL << " " << EiL;
        return 0;
    }


}

void Task4() {

    const double R1 = 205, R2 = 218, R3 = 209, R_sum = 476,
        Es_R1 = 1.9, Es_R2 = 1.4, Es_R3 = 1.2, Es_R_sum = 1.2,
        Ei_R1 = -1.2, Ei_R2 = -1.1, Ei_R3 = -1.6, Ei_R_sum = -1.7;

    double R23, R4;
    double TR1, TR2, TR3, TR4, TR_sum;
    double EmR1, EmR2, EmR3, EmR4, EmR_sum;
    double delta2, delta3;
    double EsR4, EiR4;
    double R4_max, R4_min;

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

    cout << "R4_max = " << R4_max << endl;
    cout << "R4_min = " << R4_min << endl;



}
