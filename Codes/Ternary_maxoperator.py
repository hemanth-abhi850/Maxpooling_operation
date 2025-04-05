

# Define the comparator_3t function
def Max_operator_2t(a, b):
    m=DTC2(a)
    n=DTC2(b)
    G_0, E_0 = comparator(m[0], n[0])  # 1 bit comparator
    m_0 = mux_2x1(G_0, n[0], m[0]) #1
    p=OR_max(n[1], m[1]) #or
    z = mux_2x1(G_0, n[1], m[1]) #2
    m_1 = mux_2x1(E_0, z, p) #2
    out=decimal((m_0,m_1))
    return out

def Max_operator_3t(a, b):
    m=DTC3(a)
    n=DTC3(b)
    G_0, E_0 = comparator(m[0], n[0]) # 1 bit comparator
    G_1, E_1 = comparator(m[1], n[1]) # 1 bit comparator

    G_2 = custom_max(G_0, custom_min(E_0, G_1))
    E_2 = custom_min(E_0, E_1)

    m_0 = mux_2x1(G_0, n[0], m[0]) #1
    z   = mux_2x1(G_0, n[1], m[1]) #2
    p   = OR_max(n[1], m[1]) #or
    m_1 = mux_2x1(E_0, z, p) #2

    z1  = mux_2x1(G_2, n[2], m[2]) #2
    p1   = OR_max(n[2], m[2]) #or
    m_2 = mux_2x1(E_2, z1, p1) #2

    out=decimal((m_0,m_1,m_2))
    return out

def Max_operator_4t(a, b):
    m=DTC4(a)
    n=DTC4(b)
    G_0, E_0 = comparator(m[0], n[0]) # 1 bit comparator
    G_1, E_1 = comparator(m[1], n[1]) # 1 bit comparator
    G_2, E_2 = comparator(m[2], n[2]) # 1 bit comparator

    G_01 = custom_max(G_0, custom_min(E_0, G_1))
    E_01 = custom_min(E_0, E_1)

    G_02 = custom_max(G_01, custom_min(E_01, G_2))
    E_02 = custom_min(E_01, E_2)

    m_0 = mux_2x1(G_0, n[0], m[0]) #1
    z   = mux_2x1(G_0, n[1], m[1]) #2
    p   = OR_max(n[1], m[1]) #or
    m_1 = mux_2x1(E_0, z, p) #3

    z1  = mux_2x1(G_01, n[2], m[2]) #4
    p1   = OR_max(n[2], m[2]) #or
    m_2 = mux_2x1(E_01, z1, p1) #5

    z2  = mux_2x1(G_02, n[3], m[3]) #6
    p2   = OR_max(n[3], m[3]) #or
    m_3 = mux_2x1(E_02, z2, p2) #7

    out=decimal((m_0,m_1,m_2,m_3))
    return out

def Max_operator_5t(a, b):
    m=DTC5(a)
    n=DTC5(b)
    G_0, E_0 = comparator(m[0], n[0]) # 1 bit comparator
    G_1, E_1 = comparator(m[1], n[1]) # 1 bit comparator
    G_2, E_2 = comparator(m[2], n[2]) # 1 bit comparator
    G_3, E_3 = comparator(m[3], n[3]) # 1 bit comparator

    G_01 = custom_max(G_0, custom_min(E_0, G_1))
    E_01 = custom_min(E_0, E_1)

    G_02 = custom_max(G_01, custom_min(E_01, G_2))
    E_02 = custom_min(E_01, E_2)

    G_03 = custom_max(G_02, custom_min(E_02, G_3))
    E_03 = custom_min(E_02, E_3)

    m_0 = mux_2x1(G_0, n[0], m[0]) #1
    z   = mux_2x1(G_0, n[1], m[1]) #2
    p   = OR_max(n[1], m[1]) #or
    m_1 = mux_2x1(E_0, z, p) #3

    z1  = mux_2x1(G_01, n[2], m[2]) #4
    p1   = OR_max(n[2], m[2]) #or
    m_2 = mux_2x1(E_01, z1, p1) #5

    z2  = mux_2x1(G_02, n[3], m[3]) #6
    p2   = OR_max(n[3], m[3]) #or
    m_3 = mux_2x1(E_02, z2, p2) #7

    z3  = mux_2x1(G_03, n[4], m[4]) #8
    p3   = OR_max(n[4], m[4]) #or
    m_4 = mux_2x1(E_03, z3, p3) #9
    out=decimal((m_0,m_1,m_2,m_3,m_4))
    return out


def Max_operator6(a, b):
    m=DTC6(a)
    n=DTC6(b)
    G_0, E_0 = comparator(m[0], n[0]) # 1 bit comparator
    G_1, E_1 = comparator(m[1], n[1]) # 1 bit comparator
    G_2, E_2 = comparator(m[2], n[2]) # 1 bit comparator
    G_3, E_3 = comparator(m[3], n[3]) # 1 bit comparator
    G_4, E_4 = comparator(m[4], n[4]) # 1 bit comparator

    G_01 = custom_max(G_0, custom_min(E_0, G_1))
    E_01 = custom_min(E_0, E_1)

    G_02 = custom_max(G_01, custom_min(E_01, G_2))
    E_02 = custom_min(E_01, E_2)

    G_03 = custom_max(G_02, custom_min(E_02, G_3))
    E_03 = custom_min(E_02, E_3)

    G_04 = custom_max(G_03, custom_min(E_03, G_4))
    E_04 = custom_min(E_03, E_4)

    m_0 = mux_2x1(G_0, n[0], m[0]) #1
    z   = mux_2x1(G_0, n[1], m[1]) #2
    p   = OR_max(n[1], m[1]) #or
    m_1 = mux_2x1(E_0, z, p) #3

    z1  = mux_2x1(G_01, n[2], m[2]) #4
    p1   = OR_max(n[2], m[2]) #or
    m_2 = mux_2x1(E_01, z1, p1) #5

    z2  = mux_2x1(G_02, n[3], m[3]) #6
    p2   = OR_max(n[3], m[3]) #or
    m_3 = mux_2x1(E_02, z2, p2) #7

    z3  = mux_2x1(G_03, n[4], m[4]) #8
    p3   = OR_max(n[4], m[4]) #or
    m_4 = mux_2x1(E_03, z3, p3) #9

    z4  = mux_2x1(G_04, n[5], m[5]) #10
    p4   = OR_max(n[5], m[5]) #or
    m_5 = mux_2x1(E_04, z4, p4) #11

    out=decimal((m_0,m_1,m_2,m_3,m_4,m_5))
    return out
