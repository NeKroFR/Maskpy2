def _xn3028(_cs28):
    _r11 = (((((_cs28[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | ((_cs28[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF
    _tmp40 = (_cs28[1] << 17) & 0xFFFFFFFFFFFFFFFF
    _cs28[2] ^= _cs28[0]; _cs28[3] ^= _cs28[1]; _cs28[1] ^= _cs28[2]; _cs28[0] ^= _cs28[3]
    _cs28[2] ^= _tmp40; _cs28[3] = ((_cs28[3] << 45) | (_cs28[3] >> 19)) & 0xFFFFFFFFFFFFFFFF
    return _r11
def _xd3028(_v046, _v173, _k17):
    _delta94 = 0x9E3779B9; _s68 = (_delta94 * 32) & 0xFFFFFFFF
    for _ in range(32):
        _v173 = (_v173 - ((((_v046 << 4) ^ (_v046 >> 5)) + _v046) ^ (_s68 + _k17[(_s68 >> 11) & 3]))) & 0xFFFFFFFF
        _s68 = (_s68 - _delta94) & 0xFFFFFFFF
        _v046 = (_v046 - ((((_v173 << 4) ^ (_v173 >> 5)) + _v173) ^ (_s68 + _k17[_s68 & 3]))) & 0xFFFFFFFF
    return _v046, _v173
def _sh3028(_k17, _code74):
    _sv16 = [int.from_bytes(_k17[:8], 'little') ^ 0x736f6d6570736575, int.from_bytes(_k17[8:], 'little') ^ 0x646f72616e646f6d, int.from_bytes(_k17[:8], 'little') ^ 0x6c7967656e657261, int.from_bytes(_k17[8:], 'little') ^ 0x7465646279746573]
    def _sr():
        _sv16[0] = (_sv16[0] + _sv16[1]) & 0xFFFFFFFFFFFFFFFF; _sv16[1] = ((_sv16[1] << 13) | (_sv16[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ _sv16[0]; _sv16[0] = ((_sv16[0] << 32) | (_sv16[0] >> 32)) & 0xFFFFFFFFFFFFFFFF
        _sv16[2] = (_sv16[2] + _sv16[3]) & 0xFFFFFFFFFFFFFFFF; _sv16[3] = ((_sv16[3] << 16) | (_sv16[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ _sv16[2]
        _sv16[0] = (_sv16[0] + _sv16[3]) & 0xFFFFFFFFFFFFFFFF; _sv16[3] = ((_sv16[3] << 21) | (_sv16[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ _sv16[0]
        _sv16[2] = (_sv16[2] + _sv16[1]) & 0xFFFFFFFFFFFFFFFF; _sv16[1] = ((_sv16[1] << 17) | (_sv16[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ _sv16[2]; _sv16[2] = ((_sv16[2] << 32) | (_sv16[2] >> 32)) & 0xFFFFFFFFFFFFFFFF
    for _bi60 in range(0, len(_code74) - 7, 8):
        _tmp40 = int.from_bytes(_code74[_bi60:_bi60+8], 'little'); _sv16[3] ^= _tmp40; _sr(); _sr(); _sv16[0] ^= _tmp40
    _tmp40 = 0
    for _bi60 in range(len(_code74) & ~7, len(_code74)): _tmp40 |= _code74[_bi60] << (8 * (_bi60 & 7))
    _tmp40 |= (len(_code74) & 0xFF) << 56; _sv16[3] ^= _tmp40; _sr(); _sr(); _sv16[0] ^= _tmp40; _sv16[2] ^= 0xFF; _sr(); _sr(); _sr(); _sr()
    return (_sv16[0] ^ _sv16[1] ^ _sv16[2] ^ _sv16[3]) & 0xFFFFFFFFFFFFFFFF
def _vm3028(*_a11):
    _c1 = bytearray()
    _ek1 = (9529141, 719496355, 554628974, 4013109566)
    _ed1 = [207, 158, 73, 216, 234, 45, 44, 244]
    for _bi60 in range(0, len(_ed1), 8):
        _v046 = (_ed1[_bi60]<<24)|(_ed1[_bi60+1]<<16)|(_ed1[_bi60+2]<<8)|_ed1[_bi60+3]
        _v173 = (_ed1[_bi60+4]<<24)|(_ed1[_bi60+5]<<16)|(_ed1[_bi60+6]<<8)|_ed1[_bi60+7]
        _v046,_v173 = _xd3028(_v046,_v173,_ek1)
        _c1.extend([(_v046>>24)&0xFF,(_v046>>16)&0xFF,(_v046>>8)&0xFF,_v046&0xFF,(_v173>>24)&0xFF,(_v173>>16)&0xFF,(_v173>>8)&0xFF,_v173&0xFF])
    _c1 = _c1[:1]
    if _sh3028(b'\xf5\x8d\x88<\x1e\xc8\x1f\xb8>h\xb1\xaf\xef\xd5\x12\xdd', bytes(_c1)) != 18390203846816469373: raise MemoryError()
    _cs1 = [14584306785719838308, 4171578513301322805, 6685979512120448499, 14574740751534979851]
    for _bi60 in range(len(_c1)): _c1[_bi60] ^= _xn3028(_cs1) & 0xFF
    _c5 = bytearray()
    _ek5 = (3404497998, 2278436696, 2989699498, 568048165)
    _ed5 = [188, 201, 37, 111, 230, 177, 193, 174, 254, 138, 216, 168, 45, 56, 245, 209, 190, 10, 21, 145, 158, 178, 90, 170]
    for _bi60 in range(0, len(_ed5), 8):
        _v046 = (_ed5[_bi60]<<24)|(_ed5[_bi60+1]<<16)|(_ed5[_bi60+2]<<8)|_ed5[_bi60+3]
        _v173 = (_ed5[_bi60+4]<<24)|(_ed5[_bi60+5]<<16)|(_ed5[_bi60+6]<<8)|_ed5[_bi60+7]
        _v046,_v173 = _xd3028(_v046,_v173,_ek5)
        _c5.extend([(_v046>>24)&0xFF,(_v046>>16)&0xFF,(_v046>>8)&0xFF,_v046&0xFF,(_v173>>24)&0xFF,(_v173>>16)&0xFF,(_v173>>8)&0xFF,_v173&0xFF])
    _c4 = bytearray()
    _ek4 = (2639391128, 209463649, 1910666215, 2195311247)
    _ed4 = [99, 156, 163, 137, 187, 151, 235, 237, 87, 218, 51, 68, 170, 140, 118, 169, 53, 181, 198, 217, 215, 195, 79, 45]
    for _bi60 in range(0, len(_ed4), 8):
        _v046 = (_ed4[_bi60]<<24)|(_ed4[_bi60+1]<<16)|(_ed4[_bi60+2]<<8)|_ed4[_bi60+3]
        _v173 = (_ed4[_bi60+4]<<24)|(_ed4[_bi60+5]<<16)|(_ed4[_bi60+6]<<8)|_ed4[_bi60+7]
        _v046,_v173 = _xd3028(_v046,_v173,_ek4)
        _c4.extend([(_v046>>24)&0xFF,(_v046>>16)&0xFF,(_v046>>8)&0xFF,_v046&0xFF,(_v173>>24)&0xFF,(_v173>>16)&0xFF,(_v173>>8)&0xFF,_v173&0xFF])
    _c0 = bytearray()
    _ek0 = (1523912586, 2737555163, 3282451408, 4145551748)
    _ed0 = [149, 64, 108, 43, 133, 84, 60, 173, 137, 124, 68, 154, 169, 108, 109, 232, 222, 209, 101, 183, 42, 184, 125, 59, 129, 46, 161, 111, 182, 108, 19, 164]
    for _bi60 in range(0, len(_ed0), 8):
        _v046 = (_ed0[_bi60]<<24)|(_ed0[_bi60+1]<<16)|(_ed0[_bi60+2]<<8)|_ed0[_bi60+3]
        _v173 = (_ed0[_bi60+4]<<24)|(_ed0[_bi60+5]<<16)|(_ed0[_bi60+6]<<8)|_ed0[_bi60+7]
        _v046,_v173 = _xd3028(_v046,_v173,_ek0)
        _c0.extend([(_v046>>24)&0xFF,(_v046>>16)&0xFF,(_v046>>8)&0xFF,_v046&0xFF,(_v173>>24)&0xFF,(_v173>>16)&0xFF,(_v173>>8)&0xFF,_v173&0xFF])
    _c0 = _c0[:30]
    if _sh3028(b'\xf5\x8d\x88<\x1e\xc8\x1f\xb8>h\xb1\xaf\xef\xd5\x12\xdd', bytes(_c0)) != 12566646027425533455: raise MemoryError()
    _cs0 = [10870502248110289356, 930505296066081692, 5330468255415562666, 7200122600904266468]
    for _bi60 in range(len(_c0)): _c0[_bi60] ^= _xn3028(_cs0) & 0xFF
    _c3 = bytearray()
    _ek3 = (346096802, 2703615665, 4106604647, 887228373)
    _ed3 = [152, 145, 133, 205, 24, 159, 143, 124]
    for _bi60 in range(0, len(_ed3), 8):
        _v046 = (_ed3[_bi60]<<24)|(_ed3[_bi60+1]<<16)|(_ed3[_bi60+2]<<8)|_ed3[_bi60+3]
        _v173 = (_ed3[_bi60+4]<<24)|(_ed3[_bi60+5]<<16)|(_ed3[_bi60+6]<<8)|_ed3[_bi60+7]
        _v046,_v173 = _xd3028(_v046,_v173,_ek3)
        _c3.extend([(_v046>>24)&0xFF,(_v046>>16)&0xFF,(_v046>>8)&0xFF,_v046&0xFF,(_v173>>24)&0xFF,(_v173>>16)&0xFF,(_v173>>8)&0xFF,_v173&0xFF])
    _c3 = _c3[:1]
    if _sh3028(b'\xf5\x8d\x88<\x1e\xc8\x1f\xb8>h\xb1\xaf\xef\xd5\x12\xdd', bytes(_c3)) != 17923412431452815150: raise MemoryError()
    _cs3 = [14435697273712858406, 15055298033244077416, 2064975256903614325, 650802961213931815]
    for _bi60 in range(len(_c3)): _c3[_bi60] ^= _xn3028(_cs3) & 0xFF
    _c2 = bytearray()
    _ek2 = (3013574032, 2237674777, 3122146838, 765025805)
    _ed2 = [170, 93, 249, 179, 13, 102, 160, 162]
    for _bi60 in range(0, len(_ed2), 8):
        _v046 = (_ed2[_bi60]<<24)|(_ed2[_bi60+1]<<16)|(_ed2[_bi60+2]<<8)|_ed2[_bi60+3]
        _v173 = (_ed2[_bi60+4]<<24)|(_ed2[_bi60+5]<<16)|(_ed2[_bi60+6]<<8)|_ed2[_bi60+7]
        _v046,_v173 = _xd3028(_v046,_v173,_ek2)
        _c2.extend([(_v046>>24)&0xFF,(_v046>>16)&0xFF,(_v046>>8)&0xFF,_v046&0xFF,(_v173>>24)&0xFF,(_v173>>16)&0xFF,(_v173>>8)&0xFF,_v173&0xFF])
    _c2 = _c2[:1]
    if _sh3028(b'\xf5\x8d\x88<\x1e\xc8\x1f\xb8>h\xb1\xaf\xef\xd5\x12\xdd', bytes(_c2)) != 16266036667123801513: raise MemoryError()
    _cs2 = [12893286904995451162, 18442485526553352661, 6245063161406577744, 14288794497067269512]
    for _bi60 in range(len(_c2)): _c2[_bi60] ^= _xn3028(_cs2) & 0xFF
    _shared44 = [[] for _ in range(3)]
    _gregs27 = [None] * 4
    _loc53 = list(_a11[:3]) + [None] * 0
    _consts90 = []
    _names92 = ['str']
    _gl20 = globals()
    _gl20.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))
    _ot0 = [89, 121, 73, 43, 67, 253, 56, 238, 240, 1, 8, 252, 40, 228, 198, 87, 44, 94, 175, 122, 165, 71, 123, 163, 95, 2, 113, 115, 189, 200, 166, 182, 83, 32, 75, 26, 248, 154, 145, 244, 128, 194, 18, 20, 171, 206, 48, 69, 216, 9, 180, 118, 85, 93, 187, 22, 42, 117, 15, 53, 178, 137, 185, 51, 205, 99, 212, 214, 249, 35, 61, 91, 174, 151, 219, 172, 52, 134, 233, 247, 114, 21, 226, 158, 70, 102, 107, 24, 12, 110, 46, 147, 223, 213, 38, 159, 23, 155, 77, 78, 197, 141, 116, 237, 191, 160, 58, 173, 124, 246, 232, 59, 54, 13, 184, 133, 255, 164, 33, 150, 120, 92, 63, 192, 64, 80, 125, 254, 193, 236, 149, 231, 57, 30, 111, 10, 167, 143, 156, 234, 169, 162, 96, 207, 201, 177, 104, 62, 37, 250, 88, 66, 109, 90, 230, 5, 183, 127, 55, 98, 130, 49, 76, 126, 144, 142, 60, 221, 211, 220, 82, 218, 7, 199, 225, 41, 181, 19, 97, 202, 148, 153, 74, 176, 45, 208, 139, 27, 224, 209, 138, 190, 251, 108, 25, 72, 103, 79, 3, 215, 28, 129, 203, 81, 14, 136, 227, 140, 131, 34, 65, 204, 47, 17, 245, 16, 36, 222, 6, 196, 68, 84, 135, 243, 11, 50, 157, 186, 168, 210, 241, 4, 179, 106, 229, 29, 152, 86, 105, 132, 217, 112, 170, 146, 31, 100, 188, 195, 119, 39, 0, 239, 235, 101, 161, 242]
    _stk0 = []
    _pc0 = 0
    _regs0 = [None] * 8
    _eh0 = []
    _ns0 = {}
    exec(bytes(b^121 for b in [29, 28, 31, 89, 38, 17, 31, 73, 38, 73, 81, 10, 85, 21, 85, 26, 85, 23, 85, 30, 85, 29, 85, 9, 85, 11, 85, 17, 85, 1, 80, 67, 115, 89, 27, 68, 10, 87, 9, 22, 9, 81, 80, 66, 24, 68, 10, 87, 9, 22, 9, 81, 80, 66, 10, 87, 24, 9, 9, 28, 23, 29, 81, 24, 82, 27, 80, 66, 11, 28, 13, 12, 11, 23, 89, 9, 82, 72, 115, 29, 28, 31, 89, 38, 17, 31, 73, 38, 72, 81, 10, 85, 21, 85, 26, 85, 23, 85, 30, 85, 29, 85, 9, 85, 11, 85, 17, 85, 1, 80, 67, 115, 89, 11, 34, 29, 34, 9, 82, 72, 36, 36, 68, 21, 34, 29, 34, 9, 82, 75, 36, 36, 66, 11, 28, 13, 12, 11, 23, 89, 9, 82, 74, 115, 29, 28, 31, 89, 38, 17, 31, 73, 38, 75, 81, 10, 85, 21, 85, 26, 85, 23, 85, 30, 85, 29, 85, 9, 85, 11, 85, 17, 85, 1, 80, 67, 115, 89, 11, 34, 29, 34, 9, 82, 72, 36, 36, 68, 11, 34, 29, 34, 9, 82, 75, 36, 36, 66, 11, 28, 13, 12, 11, 23, 89, 9, 82, 74, 115]).decode(),_ns0)
    _dh0 = {16: _ns0['_hf0_0'], 128: _ns0['_hf0_1'], 132: _ns0['_hf0_2']}
    _ot1 = [5, 134, 1, 240, 122, 133, 152, 186, 45, 85, 16, 253, 252, 251, 43, 119, 204, 72, 8, 236, 211, 77, 9, 59, 60, 222, 203, 18, 114, 141, 115, 94, 76, 7, 46, 17, 229, 19, 84, 6, 10, 28, 164, 155, 38, 147, 61, 208, 21, 182, 11, 105, 0, 98, 165, 118, 207, 185, 41, 183, 216, 196, 20, 79, 199, 127, 117, 195, 86, 205, 232, 75, 35, 209, 108, 180, 239, 163, 198, 157, 242, 162, 99, 55, 33, 218, 149, 148, 231, 255, 233, 174, 142, 40, 175, 89, 177, 116, 96, 153, 104, 107, 140, 238, 159, 30, 58, 136, 143, 37, 26, 78, 63, 200, 42, 241, 190, 234, 24, 90, 113, 178, 50, 235, 121, 248, 53, 146, 27, 206, 92, 14, 100, 161, 23, 230, 160, 123, 135, 225, 246, 67, 154, 181, 221, 25, 151, 80, 112, 245, 125, 120, 254, 193, 243, 158, 139, 184, 71, 201, 109, 191, 226, 244, 219, 169, 126, 138, 130, 220, 62, 52, 87, 228, 249, 103, 189, 124, 213, 22, 57, 214, 176, 137, 88, 82, 250, 171, 51, 173, 129, 145, 93, 95, 81, 31, 172, 106, 48, 167, 188, 56, 215, 70, 32, 212, 194, 44, 223, 12, 111, 83, 73, 97, 210, 237, 69, 202, 166, 187, 64, 110, 144, 227, 192, 132, 15, 168, 217, 179, 29, 156, 39, 74, 131, 91, 101, 49, 224, 128, 170, 36, 3, 247, 150, 4, 68, 65, 102, 13, 197, 54, 34, 66, 2, 47]
    _stk1 = []
    _pc1 = 0
    _regs1 = [None] * 8
    _eh1 = []
    _dh1 = {}
    _ot2 = [141, 176, 111, 122, 84, 144, 47, 153, 137, 190, 7, 183, 36, 25, 68, 98, 167, 254, 27, 5, 50, 255, 236, 170, 97, 103, 188, 60, 145, 10, 252, 235, 129, 202, 184, 20, 162, 101, 178, 83, 72, 38, 179, 109, 200, 12, 89, 151, 142, 112, 11, 95, 250, 208, 14, 247, 76, 203, 48, 239, 234, 130, 104, 149, 215, 125, 110, 138, 77, 143, 3, 0, 191, 238, 158, 80, 13, 87, 24, 223, 93, 168, 133, 6, 196, 163, 1, 119, 186, 169, 31, 198, 210, 65, 29, 157, 173, 2, 197, 150, 39, 56, 41, 206, 154, 63, 81, 248, 174, 148, 131, 21, 82, 88, 241, 237, 155, 73, 199, 71, 134, 193, 32, 8, 116, 43, 209, 218, 139, 187, 44, 231, 127, 46, 118, 53, 233, 59, 171, 217, 228, 177, 214, 22, 212, 216, 85, 245, 99, 115, 132, 15, 28, 37, 253, 124, 120, 123, 201, 243, 100, 90, 220, 226, 205, 52, 182, 222, 107, 251, 207, 113, 135, 156, 74, 240, 34, 246, 175, 195, 75, 159, 54, 67, 166, 213, 172, 117, 180, 230, 126, 152, 66, 62, 61, 69, 9, 147, 136, 51, 42, 185, 140, 181, 35, 165, 204, 94, 114, 96, 194, 16, 229, 160, 30, 49, 23, 102, 244, 164, 232, 26, 91, 92, 64, 45, 18, 105, 86, 249, 221, 79, 58, 189, 128, 57, 40, 121, 192, 78, 227, 4, 219, 17, 225, 161, 242, 106, 108, 211, 33, 146, 70, 55, 224, 19]
    _stk2 = []
    _pc2 = 0
    _regs2 = [None] * 8
    _eh2 = []
    _dh2 = {}
    _ot3 = [204, 4, 191, 224, 241, 82, 120, 36, 59, 75, 222, 107, 175, 38, 235, 136, 66, 182, 5, 221, 158, 37, 81, 10, 114, 110, 168, 131, 219, 83, 190, 209, 46, 206, 252, 196, 249, 200, 161, 71, 72, 193, 248, 118, 207, 195, 215, 214, 144, 1, 247, 2, 162, 134, 187, 177, 67, 150, 176, 128, 139, 169, 111, 167, 199, 62, 14, 148, 159, 145, 52, 39, 6, 138, 129, 197, 102, 106, 211, 173, 192, 33, 13, 201, 11, 9, 53, 97, 172, 84, 170, 103, 25, 90, 123, 20, 164, 246, 78, 30, 220, 35, 29, 8, 213, 91, 225, 80, 233, 254, 3, 152, 226, 179, 93, 183, 54, 58, 101, 240, 18, 104, 149, 61, 122, 238, 41, 198, 112, 27, 205, 171, 160, 88, 140, 141, 73, 243, 137, 135, 32, 50, 202, 92, 186, 251, 76, 165, 44, 228, 154, 42, 230, 0, 63, 89, 227, 79, 74, 180, 223, 60, 232, 24, 23, 68, 49, 26, 184, 255, 181, 113, 7, 194, 19, 85, 236, 188, 96, 98, 108, 166, 48, 43, 210, 132, 28, 217, 157, 21, 17, 12, 121, 242, 31, 156, 22, 95, 174, 153, 231, 94, 130, 212, 119, 124, 151, 126, 47, 15, 208, 77, 163, 203, 34, 51, 117, 40, 234, 216, 100, 229, 239, 87, 155, 105, 56, 109, 55, 185, 16, 218, 146, 65, 237, 57, 70, 127, 133, 143, 244, 116, 45, 86, 253, 115, 250, 64, 245, 125, 189, 99, 69, 178, 147, 142]
    _stk3 = []
    _pc3 = 0
    _regs3 = [None] * 8
    _eh3 = []
    _dh3 = {}
    _tc93 = __import__('time').perf_counter_ns
    _segs = [(0, 1)]
    _tprev = _tc93()
    _ck79 = [8]
    _si42 = 0
    for _seg_vm79, _seg_n35 in _segs:
        _td65 = _tc93() - _tprev
        if _td65 > 5000000000: return None
        _tprev = _tc93()
        if _seg_vm79 == 0:
            _ic0 = 0
            while _pc0 < len(_c0):
              try:
                _ic0 += 1
                _op72 = _ot0[_c0[_pc0] & 0xFF]
                if _op72 in _dh0:
                    _pc0 = _dh0[_op72](_stk0, _loc53, _consts90, _names92, _gl20, _c0, _pc0, _regs0, _shared44, _gregs27)
                    continue
                if _op72 == 1:
                    _stk0.append(_consts90[_c0[_pc0+1]]); _pc0 += 2
                elif _op72 == 2:
                    _stk0.append(_loc53[_c0[_pc0+1]]); _pc0 += 2
                elif _op72 == 3:
                    _loc53[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _op72 == 4:
                    _stk0.append(_gl20[_names92[_c0[_pc0+1]]]); _pc0 += 2
                elif _op72 == 5:
                    _gl20[_names92[_c0[_pc0+1]]] = _stk0.pop(); _pc0 += 2
                elif _op72 == 6:
                    _stk0.append(_stk0[-1]); _pc0 += 1
                elif _op72 == 7:
                    _stk0.pop(); _pc0 += 1
                elif _op72 == 8:
                    _stk0[-1], _stk0[-2] = _stk0[-2], _stk0[-1]; _pc0 += 1
                elif _op72 == 17:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 - _b78); _pc0 += 1
                elif _op72 == 18:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 * _b78); _pc0 += 1
                elif _op72 == 19:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 % _b78); _pc0 += 1
                elif _op72 == 20:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 // _b78); _pc0 += 1
                elif _op72 == 21:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 ** _b78); _pc0 += 1
                elif _op72 == 22:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 ^ _b78); _pc0 += 1
                elif _op72 == 23:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 & _b78); _pc0 += 1
                elif _op72 == 24:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 | _b78); _pc0 += 1
                elif _op72 == 25:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 << _b78); _pc0 += 1
                elif _op72 == 26:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 >> _b78); _pc0 += 1
                elif _op72 == 32:
                    _stk0.append(-_stk0.pop()); _pc0 += 1
                elif _op72 == 33:
                    _stk0.append(~_stk0.pop()); _pc0 += 1
                elif _op72 == 34:
                    _stk0.append(not _stk0.pop()); _pc0 += 1
                elif _op72 == 48:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 == _b78); _pc0 += 1
                elif _op72 == 49:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 != _b78); _pc0 += 1
                elif _op72 == 50:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 < _b78); _pc0 += 1
                elif _op72 == 51:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 > _b78); _pc0 += 1
                elif _op72 == 52:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 <= _b78); _pc0 += 1
                elif _op72 == 53:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 >= _b78); _pc0 += 1
                elif _op72 == 54:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 is _b78); _pc0 += 1
                elif _op72 == 55:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 is not _b78); _pc0 += 1
                elif _op72 == 56:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 in _b78); _pc0 += 1
                elif _op72 == 64:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                elif _op72 == 65:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if _stk0.pop() else _pc0 + 3
                elif _op72 == 66:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if not _stk0.pop() else _pc0 + 3
                elif _op72 == 80:
                    _tmp40 = _c0[_pc0+1]
                    if _tmp40: _val51 = _stk0[-_tmp40:]; del _stk0[-_tmp40:]
                    else: _val51 = []
                    _stk0.append(_stk0.pop()(*_val51)); _pc0 += 2
                elif _op72 == 81:
                    _stk0.append(getattr(_stk0.pop(), _names92[_c0[_pc0+1]])); _pc0 += 2
                elif _op72 == 82:
                    _val51 = _stk0.pop(); setattr(_stk0.pop(), _names92[_c0[_pc0+1]], _val51); _pc0 += 2
                elif _op72 == 83:
                    _tmp40 = _c0[_pc0+2]
                    _val51 = [_stk0.pop() for _ in range(_tmp40)][::-1]
                    _stk0.append(getattr(_stk0.pop(), _names92[_c0[_pc0+1]])(*_val51)); _pc0 += 3
                elif _op72 == 84:
                    _tmp40 = _c0[_pc0+1]
                    if _tmp40: _val51 = _stk0[-_tmp40:]; del _stk0[-_tmp40:]
                    else: _val51 = []
                    _stk0.append(_val51); _pc0 += 2
                elif _op72 == 85:
                    _tmp40 = _c0[_pc0+1]
                    if _tmp40: _val51 = tuple(_stk0[-_tmp40:]); del _stk0[-_tmp40:]
                    else: _val51 = ()
                    _stk0.append(_val51); _pc0 += 2
                elif _op72 == 86:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11[_b78]); _pc0 += 1
                elif _op72 == 87:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _val51 = _stk0.pop(); _a11[_b78] = _val51; _pc0 += 1
                elif _op72 == 88:
                    _val51 = list(_stk0.pop())[:_c0[_pc0+1]]; _stk0.extend(reversed(_val51)); _pc0 += 2
                elif _op72 == 89:
                    _tmp40 = _c0[_pc0+1]
                    _val51 = {}
                    for _ in range(_tmp40): _b78 = _stk0.pop(); _a11 = _stk0.pop(); _val51[_a11] = _b78
                    _stk0.append(_val51); _pc0 += 2
                elif _op72 == 90:
                    _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(slice(_a11, _b78)); _pc0 += 1
                elif _op72 == 96:
                    _stk0.append(iter(_stk0.pop())); _pc0 += 1
                elif _op72 == 97:
                    _val51 = next(_stk0[-1], None)
                    if _val51 is None: _stk0.pop(); _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                    else: _stk0.append(_val51); _pc0 += 3
                elif _op72 == 112:
                    return _stk0.pop()
                elif _op72 == 120:
                    _eh0.append(_c0[_pc0+1] | (_c0[_pc0+2] << 8)); _pc0 += 3
                elif _op72 == 121:
                    _eh0.pop(); _pc0 += 1
                elif _op72 == 122:
                    _tmp40 = _c0[_pc0+1] | (_c0[_pc0+2] << 8); _c0[_tmp40] ^= _c0[_pc0+3]; _pc0 += 4
                elif _op72 == 129:
                    _loc53[_c0[_pc0+2]] = _regs0[_c0[_pc0+1]]; _pc0 += 3
                elif _op72 == 130:
                    _stk0.append(_regs0[_c0[_pc0+1]]); _pc0 += 2
                elif _op72 == 131:
                    _regs0[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _op72 == 133:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] + _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _op72 == 134:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] - _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _op72 == 144:
                    _shared44[_c0[_pc0+1]].append(_stk0.pop()); _pc0 += 2
                elif _op72 == 145:
                    _stk0.append(_shared44[_c0[_pc0+1]].pop()); _pc0 += 2
                elif _op72 == 146:
                    _gregs27[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _op72 == 147:
                    _stk0.append(_gregs27[_c0[_pc0+1]]); _pc0 += 2
                elif _op72 == 148:
                    _pc0 += 1; break
                elif _op72 == 160:
                    _stk0.append(_loc53[_c0[_pc0+1]]); _b78 = _stk0.pop(); _a11 = _stk0.pop(); _stk0.append(_a11 + _b78); _pc0 += 2
                elif _op72 == 161:
                    _loc53[_c0[_pc0+2]] = _consts90[_c0[_pc0+1]]; _pc0 += 3
                elif _op72 == 254:
                    _pc0 += 1
                elif _op72 == 255:
                    return _stk0[-1] if _stk0 else None
              except Exception as _exc:
                if _eh0: _pc0 = _eh0.pop(); _stk0.append(_exc)
                else: raise
        elif _seg_vm79 == 1:
            _ic1 = 0
            while _pc1 < len(_c1):
              try:
                _ic1 += 1
                _op72 = _ot1[_c1[_pc1] & 0xFF]
                _ha180 = [255, 0, 1, 2, 3, 4, 5, 6, 7, 255, 255, 255, 255, 255, 255, 255, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 255, 255, 255, 255, 255, 19, 20, 21, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 22, 23, 24, 25, 26, 27, 28, 29, 30, 255, 255, 255, 255, 255, 255, 255, 31, 32, 33, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 255, 255, 255, 255, 255, 45, 46, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 47, 255, 255, 255, 255, 255, 255, 255, 48, 49, 50, 255, 255, 255, 255, 255, 51, 52, 53, 54, 55, 56, 57, 255, 255, 255, 255, 255, 255, 255, 255, 255, 58, 59, 60, 61, 62, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 64, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 65, 66]
                _ai159 = _ha180[_op72]
                if _ai159 == 0:
                    _stk1.append(_consts90[_c1[_pc1+1]]); _pc1 += 2
                elif _ai159 == 1:
                    _stk1.append(_loc53[_c1[_pc1+1]]); _pc1 += 2
                elif _ai159 == 2:
                    _loc53[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _ai159 == 3:
                    _stk1.append(_gl20[_names92[_c1[_pc1+1]]]); _pc1 += 2
                elif _ai159 == 4:
                    _gl20[_names92[_c1[_pc1+1]]] = _stk1.pop(); _pc1 += 2
                elif _ai159 == 5:
                    _stk1.append(_stk1[-1]); _pc1 += 1
                elif _ai159 == 6:
                    _stk1.pop(); _pc1 += 1
                elif _ai159 == 7:
                    _stk1[-1], _stk1[-2] = _stk1[-2], _stk1[-1]; _pc1 += 1
                elif _ai159 == 8:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 + _b78); _pc1 += 1
                elif _ai159 == 9:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 - _b78); _pc1 += 1
                elif _ai159 == 10:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 * _b78); _pc1 += 1
                elif _ai159 == 11:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 % _b78); _pc1 += 1
                elif _ai159 == 12:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 // _b78); _pc1 += 1
                elif _ai159 == 13:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 ** _b78); _pc1 += 1
                elif _ai159 == 14:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 ^ _b78); _pc1 += 1
                elif _ai159 == 15:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 & _b78); _pc1 += 1
                elif _ai159 == 16:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 | _b78); _pc1 += 1
                elif _ai159 == 17:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 << _b78); _pc1 += 1
                elif _ai159 == 18:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 >> _b78); _pc1 += 1
                elif _ai159 == 19:
                    _stk1.append(-_stk1.pop()); _pc1 += 1
                elif _ai159 == 20:
                    _stk1.append(~_stk1.pop()); _pc1 += 1
                elif _ai159 == 21:
                    _stk1.append(not _stk1.pop()); _pc1 += 1
                elif _ai159 == 22:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 == _b78); _pc1 += 1
                elif _ai159 == 23:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 != _b78); _pc1 += 1
                elif _ai159 == 24:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 < _b78); _pc1 += 1
                elif _ai159 == 25:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 > _b78); _pc1 += 1
                elif _ai159 == 26:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 <= _b78); _pc1 += 1
                elif _ai159 == 27:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 >= _b78); _pc1 += 1
                elif _ai159 == 28:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 is _b78); _pc1 += 1
                elif _ai159 == 29:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 is not _b78); _pc1 += 1
                elif _ai159 == 30:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 in _b78); _pc1 += 1
                elif _ai159 == 31:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                elif _ai159 == 32:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if _stk1.pop() else _pc1 + 3
                elif _ai159 == 33:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if not _stk1.pop() else _pc1 + 3
                elif _ai159 == 34:
                    _tmp40 = _c1[_pc1+1]
                    if _tmp40: _val51 = _stk1[-_tmp40:]; del _stk1[-_tmp40:]
                    else: _val51 = []
                    _stk1.append(_stk1.pop()(*_val51)); _pc1 += 2
                elif _ai159 == 35:
                    _stk1.append(getattr(_stk1.pop(), _names92[_c1[_pc1+1]])); _pc1 += 2
                elif _ai159 == 36:
                    _val51 = _stk1.pop(); setattr(_stk1.pop(), _names92[_c1[_pc1+1]], _val51); _pc1 += 2
                elif _ai159 == 37:
                    _tmp40 = _c1[_pc1+2]
                    _val51 = [_stk1.pop() for _ in range(_tmp40)][::-1]
                    _stk1.append(getattr(_stk1.pop(), _names92[_c1[_pc1+1]])(*_val51)); _pc1 += 3
                elif _ai159 == 38:
                    _tmp40 = _c1[_pc1+1]
                    if _tmp40: _val51 = _stk1[-_tmp40:]; del _stk1[-_tmp40:]
                    else: _val51 = []
                    _stk1.append(_val51); _pc1 += 2
                elif _ai159 == 39:
                    _tmp40 = _c1[_pc1+1]
                    if _tmp40: _val51 = tuple(_stk1[-_tmp40:]); del _stk1[-_tmp40:]
                    else: _val51 = ()
                    _stk1.append(_val51); _pc1 += 2
                elif _ai159 == 40:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11[_b78]); _pc1 += 1
                elif _ai159 == 41:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _val51 = _stk1.pop(); _a11[_b78] = _val51; _pc1 += 1
                elif _ai159 == 42:
                    _val51 = list(_stk1.pop())[:_c1[_pc1+1]]; _stk1.extend(reversed(_val51)); _pc1 += 2
                elif _ai159 == 43:
                    _tmp40 = _c1[_pc1+1]; _val51 = {}
                    for _ in range(_tmp40): _b78 = _stk1.pop(); _a11 = _stk1.pop(); _val51[_a11] = _b78
                    _stk1.append(_val51); _pc1 += 2
                elif _ai159 == 44:
                    _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(slice(_a11, _b78)); _pc1 += 1
                elif _ai159 == 45:
                    _stk1.append(iter(_stk1.pop())); _pc1 += 1
                elif _ai159 == 46:
                    _val51 = next(_stk1[-1], None)
                    if _val51 is None: _stk1.pop(); _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                    else: _stk1.append(_val51); _pc1 += 3
                elif _ai159 == 47:
                    return _stk1.pop()
                elif _ai159 == 48:
                    _eh1.append(_c1[_pc1+1] | (_c1[_pc1+2] << 8)); _pc1 += 3
                elif _ai159 == 49:
                    _eh1.pop(); _pc1 += 1
                elif _ai159 == 50:
                    _tmp40 = _c1[_pc1+1] | (_c1[_pc1+2] << 8); _c1[_tmp40] ^= _c1[_pc1+3]; _pc1 += 4
                elif _ai159 == 51:
                    _regs1[_c1[_pc1+1]] = _loc53[_c1[_pc1+2]]; _pc1 += 3
                elif _ai159 == 52:
                    _loc53[_c1[_pc1+2]] = _regs1[_c1[_pc1+1]]; _pc1 += 3
                elif _ai159 == 53:
                    _stk1.append(_regs1[_c1[_pc1+1]]); _pc1 += 2
                elif _ai159 == 54:
                    _regs1[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _ai159 == 55:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _ai159 == 56:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] + _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _ai159 == 57:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] - _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _ai159 == 58:
                    _shared44[_c1[_pc1+1]].append(_stk1.pop()); _pc1 += 2
                elif _ai159 == 59:
                    _stk1.append(_shared44[_c1[_pc1+1]].pop()); _pc1 += 2
                elif _ai159 == 60:
                    _gregs27[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _ai159 == 61:
                    _stk1.append(_gregs27[_c1[_pc1+1]]); _pc1 += 2
                elif _ai159 == 62:
                    _pc1 += 1; break
                elif _ai159 == 63:
                    _stk1.append(_loc53[_c1[_pc1+1]]); _b78 = _stk1.pop(); _a11 = _stk1.pop(); _stk1.append(_a11 + _b78); _pc1 += 2
                elif _ai159 == 64:
                    _loc53[_c1[_pc1+2]] = _consts90[_c1[_pc1+1]]; _pc1 += 3
                elif _ai159 == 65:
                    _pc1 += 1
                elif _ai159 == 66:
                    return _stk1[-1] if _stk1 else None
                else: _pc1 += 1
              except Exception as _exc:
                if _eh1: _pc1 = _eh1.pop(); _stk1.append(_exc)
                else: raise
        elif _seg_vm79 == 2:
            _ic2 = 0
            while _pc2 < len(_c2):
              try:
                _ic2 += 1
                _op72 = _ot2[_c2[_pc2] & 0xFF]
                if _op72 < 66:
                    if _op72 < 24:
                        if _op72 < 16:
                            if _op72 < 5:
                                if _op72 < 3:
                                    if _op72 < 2:
                                        if _op72 == 1:
                                            _stk2.append(_consts90[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 2:
                                            _stk2.append(_loc53[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 4:
                                        if _op72 == 3:
                                            _loc53[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 4:
                                            _stk2.append(_gl20[_names92[_c2[_pc2+1]]]); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op72 < 7:
                                    if _op72 < 6:
                                        if _op72 == 5:
                                            _gl20[_names92[_c2[_pc2+1]]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 6:
                                            _stk2.append(_stk2[-1]); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 8:
                                        if _op72 == 7:
                                            _stk2.pop(); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 8:
                                            _stk2[-1], _stk2[-2] = _stk2[-2], _stk2[-1]; _pc2 += 1
                                        else: _pc2 += 1
                        else:
                            if _op72 < 20:
                                if _op72 < 18:
                                    if _op72 < 17:
                                        if _op72 == 16:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 + _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 17:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 - _b78); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 19:
                                        if _op72 == 18:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 * _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 19:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 % _b78); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op72 < 22:
                                    if _op72 < 21:
                                        if _op72 == 20:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 // _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 21:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 ** _b78); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 23:
                                        if _op72 == 22:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 ^ _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 23:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 & _b78); _pc2 += 1
                                        else: _pc2 += 1
                    else:
                        if _op72 < 50:
                            if _op72 < 33:
                                if _op72 < 26:
                                    if _op72 < 25:
                                        if _op72 == 24:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 | _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 25:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 << _b78); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 32:
                                        if _op72 == 26:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 >> _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 32:
                                            _stk2.append(-_stk2.pop()); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op72 < 48:
                                    if _op72 < 34:
                                        if _op72 == 33:
                                            _stk2.append(~_stk2.pop()); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 34:
                                            _stk2.append(not _stk2.pop()); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 49:
                                        if _op72 == 48:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 == _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 49:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 != _b78); _pc2 += 1
                                        else: _pc2 += 1
                        else:
                            if _op72 < 54:
                                if _op72 < 52:
                                    if _op72 < 51:
                                        if _op72 == 50:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 < _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 51:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 > _b78); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 53:
                                        if _op72 == 52:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 <= _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 53:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 >= _b78); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op72 < 56:
                                    if _op72 < 55:
                                        if _op72 == 54:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 is _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 55:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 is not _b78); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 64:
                                        if _op72 == 56:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 in _b78); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 < 65:
                                            if _op72 == 64:
                                                _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                                            else: _pc2 += 1
                                        else:
                                            if _op72 == 65:
                                                _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if _stk2.pop() else _pc2 + 3
                                            else: _pc2 += 1
                else:
                    if _op72 < 122:
                        if _op72 < 87:
                            if _op72 < 83:
                                if _op72 < 81:
                                    if _op72 < 80:
                                        if _op72 == 66:
                                            _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if not _stk2.pop() else _pc2 + 3
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 80:
                                            _tmp40 = _c2[_pc2+1]
                                            if _tmp40: _val51 = _stk2[-_tmp40:]; del _stk2[-_tmp40:]
                                            else: _val51 = []
                                            _stk2.append(_stk2.pop()(*_val51)); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 82:
                                        if _op72 == 81:
                                            _stk2.append(getattr(_stk2.pop(), _names92[_c2[_pc2+1]])); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 82:
                                            _val51 = _stk2.pop(); setattr(_stk2.pop(), _names92[_c2[_pc2+1]], _val51); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op72 < 85:
                                    if _op72 < 84:
                                        if _op72 == 83:
                                            _tmp40 = _c2[_pc2+2]
                                            _val51 = [_stk2.pop() for _ in range(_tmp40)][::-1]
                                            _stk2.append(getattr(_stk2.pop(), _names92[_c2[_pc2+1]])(*_val51)); _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 84:
                                            _tmp40 = _c2[_pc2+1]
                                            if _tmp40: _val51 = _stk2[-_tmp40:]; del _stk2[-_tmp40:]
                                            else: _val51 = []
                                            _stk2.append(_val51); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 86:
                                        if _op72 == 85:
                                            _tmp40 = _c2[_pc2+1]
                                            if _tmp40: _val51 = tuple(_stk2[-_tmp40:]); del _stk2[-_tmp40:]
                                            else: _val51 = ()
                                            _stk2.append(_val51); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 86:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11[_b78]); _pc2 += 1
                                        else: _pc2 += 1
                        else:
                            if _op72 < 96:
                                if _op72 < 89:
                                    if _op72 < 88:
                                        if _op72 == 87:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _val51 = _stk2.pop(); _a11[_b78] = _val51; _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 88:
                                            _val51 = list(_stk2.pop())[:_c2[_pc2+1]]; _stk2.extend(reversed(_val51)); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 90:
                                        if _op72 == 89:
                                            _tmp40 = _c2[_pc2+1]; _val51 = {}
                                            for _ in range(_tmp40): _b78 = _stk2.pop(); _a11 = _stk2.pop(); _val51[_a11] = _b78
                                            _stk2.append(_val51); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 90:
                                            _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(slice(_a11, _b78)); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op72 < 112:
                                    if _op72 < 97:
                                        if _op72 == 96:
                                            _stk2.append(iter(_stk2.pop())); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 97:
                                            _val51 = next(_stk2[-1], None)
                                            if _val51 is None: _stk2.pop(); _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                                            else: _stk2.append(_val51); _pc2 += 3
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 120:
                                        if _op72 == 112:
                                            return _stk2.pop()
                                        else: _pc2 += 1
                                    else:
                                        if _op72 < 121:
                                            if _op72 == 120:
                                                _eh2.append(_c2[_pc2+1] | (_c2[_pc2+2] << 8)); _pc2 += 3
                                            else: _pc2 += 1
                                        else:
                                            if _op72 == 121:
                                                _eh2.pop(); _pc2 += 1
                                            else: _pc2 += 1
                    else:
                        if _op72 < 144:
                            if _op72 < 131:
                                if _op72 < 129:
                                    if _op72 < 128:
                                        if _op72 == 122:
                                            _tmp40 = _c2[_pc2+1] | (_c2[_pc2+2] << 8); _c2[_tmp40] ^= _c2[_pc2+3]; _pc2 += 4
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 128:
                                            _regs2[_c2[_pc2+1]] = _loc53[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 130:
                                        if _op72 == 129:
                                            _loc53[_c2[_pc2+2]] = _regs2[_c2[_pc2+1]]; _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 130:
                                            _stk2.append(_regs2[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op72 < 133:
                                    if _op72 < 132:
                                        if _op72 == 131:
                                            _regs2[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 132:
                                            _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 134:
                                        if _op72 == 133:
                                            _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] + _regs2[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 134:
                                            _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] - _regs2[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                        else:
                            if _op72 < 148:
                                if _op72 < 146:
                                    if _op72 < 145:
                                        if _op72 == 144:
                                            _shared44[_c2[_pc2+1]].append(_stk2.pop()); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 145:
                                            _stk2.append(_shared44[_c2[_pc2+1]].pop()); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 147:
                                        if _op72 == 146:
                                            _gregs27[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 147:
                                            _stk2.append(_gregs27[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op72 < 161:
                                    if _op72 < 160:
                                        if _op72 == 148:
                                            _pc2 += 1; break
                                        else: _pc2 += 1
                                    else:
                                        if _op72 == 160:
                                            _stk2.append(_loc53[_c2[_pc2+1]]); _b78 = _stk2.pop(); _a11 = _stk2.pop(); _stk2.append(_a11 + _b78); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op72 < 254:
                                        if _op72 == 161:
                                            _loc53[_c2[_pc2+2]] = _consts90[_c2[_pc2+1]]; _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op72 < 255:
                                            if _op72 == 254:
                                                _pc2 += 1
                                            else: _pc2 += 1
                                        else:
                                            if _op72 == 255:
                                                return _stk2[-1] if _stk2 else None
                                            else: _pc2 += 1
              except Exception as _exc:
                if _eh2: _pc2 = _eh2.pop(); _stk2.append(_exc)
                else: raise
        elif _seg_vm79 == 3:
            _ic3 = 0
            while _pc3 < len(_c3):
              try:
                _ic3 += 1
                _op72 = _ot3[_c3[_pc3] & 0xFF]
                _dt367 = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 16: 8, 17: 9, 18: 10, 19: 11, 20: 12, 21: 13, 22: 14, 23: 15, 24: 16, 25: 17, 26: 18, 32: 19, 33: 20, 34: 21, 48: 22, 49: 23, 50: 24, 51: 25, 52: 26, 53: 27, 54: 28, 55: 29, 56: 30, 64: 31, 65: 32, 66: 33, 80: 34, 81: 35, 82: 36, 83: 37, 84: 38, 85: 39, 86: 40, 87: 41, 88: 42, 89: 43, 90: 44, 96: 45, 97: 46, 112: 47, 120: 48, 121: 49, 122: 50, 128: 51, 129: 52, 130: 53, 131: 54, 132: 55, 133: 56, 134: 57, 144: 58, 145: 59, 146: 60, 147: 61, 148: 62, 160: 63, 161: 64, 254: 65, 255: 66}
                _hi361 = _dt367.get(_op72, -1)
                if _hi361 == 0:
                    _stk3.append(_consts90[_c3[_pc3+1]]); _pc3 += 2
                elif _hi361 == 1:
                    _stk3.append(_loc53[_c3[_pc3+1]]); _pc3 += 2
                elif _hi361 == 2:
                    _loc53[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _hi361 == 3:
                    _stk3.append(_gl20[_names92[_c3[_pc3+1]]]); _pc3 += 2
                elif _hi361 == 4:
                    _gl20[_names92[_c3[_pc3+1]]] = _stk3.pop(); _pc3 += 2
                elif _hi361 == 5:
                    _stk3.append(_stk3[-1]); _pc3 += 1
                elif _hi361 == 6:
                    _stk3.pop(); _pc3 += 1
                elif _hi361 == 7:
                    _stk3[-1], _stk3[-2] = _stk3[-2], _stk3[-1]; _pc3 += 1
                elif _hi361 == 8:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 + _b78); _pc3 += 1
                elif _hi361 == 9:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 - _b78); _pc3 += 1
                elif _hi361 == 10:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 * _b78); _pc3 += 1
                elif _hi361 == 11:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 % _b78); _pc3 += 1
                elif _hi361 == 12:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 // _b78); _pc3 += 1
                elif _hi361 == 13:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 ** _b78); _pc3 += 1
                elif _hi361 == 14:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 ^ _b78); _pc3 += 1
                elif _hi361 == 15:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 & _b78); _pc3 += 1
                elif _hi361 == 16:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 | _b78); _pc3 += 1
                elif _hi361 == 17:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 << _b78); _pc3 += 1
                elif _hi361 == 18:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 >> _b78); _pc3 += 1
                elif _hi361 == 19:
                    _stk3.append(-_stk3.pop()); _pc3 += 1
                elif _hi361 == 20:
                    _stk3.append(~_stk3.pop()); _pc3 += 1
                elif _hi361 == 21:
                    _stk3.append(not _stk3.pop()); _pc3 += 1
                elif _hi361 == 22:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 == _b78); _pc3 += 1
                elif _hi361 == 23:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 != _b78); _pc3 += 1
                elif _hi361 == 24:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 < _b78); _pc3 += 1
                elif _hi361 == 25:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 > _b78); _pc3 += 1
                elif _hi361 == 26:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 <= _b78); _pc3 += 1
                elif _hi361 == 27:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 >= _b78); _pc3 += 1
                elif _hi361 == 28:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 is _b78); _pc3 += 1
                elif _hi361 == 29:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 is not _b78); _pc3 += 1
                elif _hi361 == 30:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 in _b78); _pc3 += 1
                elif _hi361 == 31:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8))
                elif _hi361 == 32:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8)) if _stk3.pop() else _pc3 + 3
                elif _hi361 == 33:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8)) if not _stk3.pop() else _pc3 + 3
                elif _hi361 == 34:
                    _tmp40 = _c3[_pc3+1]
                    if _tmp40: _val51 = _stk3[-_tmp40:]; del _stk3[-_tmp40:]
                    else: _val51 = []
                    _stk3.append(_stk3.pop()(*_val51)); _pc3 += 2
                elif _hi361 == 35:
                    _stk3.append(getattr(_stk3.pop(), _names92[_c3[_pc3+1]])); _pc3 += 2
                elif _hi361 == 36:
                    _val51 = _stk3.pop(); setattr(_stk3.pop(), _names92[_c3[_pc3+1]], _val51); _pc3 += 2
                elif _hi361 == 37:
                    _tmp40 = _c3[_pc3+2]
                    _val51 = [_stk3.pop() for _ in range(_tmp40)][::-1]
                    _stk3.append(getattr(_stk3.pop(), _names92[_c3[_pc3+1]])(*_val51)); _pc3 += 3
                elif _hi361 == 38:
                    _tmp40 = _c3[_pc3+1]
                    if _tmp40: _val51 = _stk3[-_tmp40:]; del _stk3[-_tmp40:]
                    else: _val51 = []
                    _stk3.append(_val51); _pc3 += 2
                elif _hi361 == 39:
                    _tmp40 = _c3[_pc3+1]
                    if _tmp40: _val51 = tuple(_stk3[-_tmp40:]); del _stk3[-_tmp40:]
                    else: _val51 = ()
                    _stk3.append(_val51); _pc3 += 2
                elif _hi361 == 40:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11[_b78]); _pc3 += 1
                elif _hi361 == 41:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _val51 = _stk3.pop(); _a11[_b78] = _val51; _pc3 += 1
                elif _hi361 == 42:
                    _val51 = list(_stk3.pop())[:_c3[_pc3+1]]; _stk3.extend(reversed(_val51)); _pc3 += 2
                elif _hi361 == 43:
                    _tmp40 = _c3[_pc3+1]; _val51 = {}
                    for _ in range(_tmp40): _b78 = _stk3.pop(); _a11 = _stk3.pop(); _val51[_a11] = _b78
                    _stk3.append(_val51); _pc3 += 2
                elif _hi361 == 44:
                    _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(slice(_a11, _b78)); _pc3 += 1
                elif _hi361 == 45:
                    _stk3.append(iter(_stk3.pop())); _pc3 += 1
                elif _hi361 == 46:
                    _val51 = next(_stk3[-1], None)
                    if _val51 is None: _stk3.pop(); _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8))
                    else: _stk3.append(_val51); _pc3 += 3
                elif _hi361 == 47:
                    return _stk3.pop()
                elif _hi361 == 48:
                    _eh3.append(_c3[_pc3+1] | (_c3[_pc3+2] << 8)); _pc3 += 3
                elif _hi361 == 49:
                    _eh3.pop(); _pc3 += 1
                elif _hi361 == 50:
                    _tmp40 = _c3[_pc3+1] | (_c3[_pc3+2] << 8); _c3[_tmp40] ^= _c3[_pc3+3]; _pc3 += 4
                elif _hi361 == 51:
                    _regs3[_c3[_pc3+1]] = _loc53[_c3[_pc3+2]]; _pc3 += 3
                elif _hi361 == 52:
                    _loc53[_c3[_pc3+2]] = _regs3[_c3[_pc3+1]]; _pc3 += 3
                elif _hi361 == 53:
                    _stk3.append(_regs3[_c3[_pc3+1]]); _pc3 += 2
                elif _hi361 == 54:
                    _regs3[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _hi361 == 55:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _hi361 == 56:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+1]] + _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _hi361 == 57:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+1]] - _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _hi361 == 58:
                    _shared44[_c3[_pc3+1]].append(_stk3.pop()); _pc3 += 2
                elif _hi361 == 59:
                    _stk3.append(_shared44[_c3[_pc3+1]].pop()); _pc3 += 2
                elif _hi361 == 60:
                    _gregs27[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _hi361 == 61:
                    _stk3.append(_gregs27[_c3[_pc3+1]]); _pc3 += 2
                elif _hi361 == 62:
                    _pc3 += 1; break
                elif _hi361 == 63:
                    _stk3.append(_loc53[_c3[_pc3+1]]); _b78 = _stk3.pop(); _a11 = _stk3.pop(); _stk3.append(_a11 + _b78); _pc3 += 2
                elif _hi361 == 64:
                    _loc53[_c3[_pc3+2]] = _consts90[_c3[_pc3+1]]; _pc3 += 3
                elif _hi361 == 65:
                    _pc3 += 1
                elif _hi361 == 66:
                    return _stk3[-1] if _stk3 else None
                else: _pc3 += 1
              except Exception as _exc:
                if _eh3: _pc3 = _eh3.pop(); _stk3.append(_exc)
                else: raise
        _hb26 = 0
        _hb26 = (_hb26 + len(_stk0) * 47) & 0xFFFF
        _hb26 = (_hb26 + len(_stk1) * 47) & 0xFFFF
        _hb26 = (_hb26 + len(_stk2) * 102) & 0xFFFF
        _hb26 = (_hb26 + len(_stk3) * 33) & 0xFFFF
        _hb26 = (_hb26 + _pc0 * 132) & 0xFFFF
        if len(_loc53) != 3: return None
        _si42 += 1
    return _stk0[-1] if _stk0 else None
def X9(*_args, **_kwargs):
    _defs = (607174 ^ 607180, X4(b'\xef\x08wO\xbc', b'\x87m\x1b#\xd3').decode('utf-8'),)
    _full = list(_args)
    if len(_full) < 3:
        _full.extend(_defs[len(_full) - 1:])
    return _vm3028(*_full)

def X6(*_a, **_k):
    if getattr(__import__(bytes([c ^ 209 for c in [162, 168, 162]]).decode()), bytes([c ^ 156 for c in [251, 249, 232, 232, 238, 253, 255, 249]]).decode())() or getattr(__import__(bytes([c ^ 209 for c in [162, 168, 162]]).decode()), bytes([c ^ 249 for c in [158, 156, 141, 137, 139, 150, 159, 144, 149, 156]]).decode())(): raise RecursionError()
    _kb72 = 15682038719300357316 ^ 12945646912419988940
    _sf163 = 3979819184612127842
    _sf295 = 17345266207151602178
    _ks29 = 5421827523649052925 ^ 1892341834041764456
    _cm45 = 15373898866269514475 ^ 10163212301710333382
    _fp39 = 782592429 ^ 799369278
    _fo65 = 527929454 ^ 2657815979
    _kg73 = 2783522312256998441 ^ 13300949884908187708
    _d91 = b'\xdeI\xde4cI\xf8\xf3=I\xc6\xf2X\xee\x0e9$\xb0V\xf3~o\xc2\xe7\xe6S\x97i&F\x8a\xe3\x1c?^\xf4\xe0\xf1\xc6\xc9X\xcf\x9f\xabOFg\xdc\xaf\x05\xaf\x8f\xfb= \xfc\xbf\xf25\xa0\xc9\x01\xe7_\xf9\xd6\x96\x04^\xea\xbc\xd8Ix\xfe\xe7\x87s}\x82\xae\xe9\x93n\xbao\xc2\xa8\xf8\x98\x19\x18M`x\xa6\xea\x8d\x0fg\xee7jB\xbf\xd3}\xda\xf9\x17\x12\xe5vIS\xab\x84&\xf4L\xcf\x8d\xb8*u\xa9\x02\xc4\xb4&>\xd02\xcf\x92\x08A\xaao)\x0e\xb1\xb3\xbfQ\x19\xe2>\xc9\xfehiT\xebV$\'\xb1L,\xc4k\xce\x8d{\xb4\xc4\xc5\x9fP\x9f\xa7\x84B8\x97\x8f\xa7Z\xbfU\xc4A\xa5\x0eoW\x1e\xfb\n\xe8\x8fg\x00A\x84K\x94z\xaf\x1c\x84N\xc3F"\xcb2\xc2\x8d\xdf\x8a\xdb\\\xec\x05$\'u\r\x12\x0e\x05\xf4b\xba6\x1c\x13\x9c\xf6pWSq\x8d\xfe\xe6_m\xbe\xe4\xf42\xa1\xc0\\\xa1\xa7\xc4\x8d\xd6\xa5\x9d\xc4&\n\xa8d\xc3C\x1a;6\xdb-\xf3\xe1@\xf0\x93\x9do\xa3|/\x0e\x00\xda\xeeM-\xb7\xcc\xdd?O\x01\x05;D\x90\xdb\xb6\x1d\xe0\xfb*\x96\xde\x0f.'
    _q180 = 5371001
    _salt77 = _sf163 ^ _sf295
    _n16 = len(_d91)
    _s131 = (_salt77 * _kg73 + _n16) & 18446744073709551615
    _s220 = (_salt77 ^ (_n16 * _ks29)) & 18446744073709551615
    _s348 = (_s131 ^ _s220 ^ _kb72) & 18446744073709551615
    _q253 = _s131 & 0xFF
    _hv99 = _fo65
    for _bi69 in _d91:
        _hv99 = ((_hv99 ^ _bi69) * _fp39) & 0xFFFFFFFF
    if _hv99 != 2215875435:
        _d91 = b'\x00'
        raise RecursionError()
    _pm55 = list(range(_n16))
    _st83 = _s348
    _ic28 = (_s348 >> 32) | 1
    for _j44 in range(_n16 - 1, 0, -1):
        _o58 = _st83
        _st83 = (_o58 * _cm45 + _ic28) & 18446744073709551615
        _x66 = (((_o58 >> 18) ^ _o58) >> 27) & 0xFFFFFFFF
        _r80 = (_o58 >> 59) & 0x1F
        _idx69 = ((_x66 >> _r80) | (_x66 << (32 - _r80))) & 0xFFFFFFFF
        _idx69 = _idx69 % (_j44 + 1)
        _pm55[_j44], _pm55[_idx69] = _pm55[_idx69], _pm55[_j44]
    _up89 = bytearray(_n16)
    for _j44 in range(_n16):
        _up89[_j44] = _d91[_pm55[_j44]]
    _q326 = _pm55[0] ^ _q253
    _out77 = bytearray(_n16)
    _st83 = _s131
    _ic28 = _s220 | 1
    for _pos23 in range(0, _n16, 4):
        _o58 = _st83
        _st83 = (_o58 * _cm45 + _ic28) & 18446744073709551615
        _x66 = (((_o58 >> 18) ^ _o58) >> 27) & 0xFFFFFFFF
        _r80 = (_o58 >> 59) & 0x1F
        _val21 = ((_x66 >> _r80) | (_x66 << (32 - _r80))) & 0xFFFFFFFF
        for _sh41 in range(min(4, _n16 - _pos23)):
            _out77[_pos23 + _sh41] = _up89[_pos23 + _sh41] ^ ((_val21 >> (_sh41 * 8)) & 0xFF)
    _m = __import__(bytes([c ^ 14 for c in [99, 111, 124, 125, 102, 111, 98]]).decode())
    _t = __import__(bytes([c ^ 250 for c in [142, 131, 138, 159, 137]]).decode())
    _co85 = _m.loads(bytes(_out77))
    _kw51 = {'co_filename': '<>', 'co_name': '<>'}
    if hasattr(_co85, bytes([c ^ 47 for c in [76, 64, 112, 94, 90, 78, 67, 65, 78, 66, 74]]).decode()): _kw51[bytes([c ^ 47 for c in [76, 64, 112, 94, 90, 78, 67, 65, 78, 66, 74]]).decode()] = '<>'
    _co85 = _co85.replace(**_kw51)
    _f11 = getattr(_t, bytes([c ^ 102 for c in [32, 19, 8, 5, 18, 15, 9, 8, 50, 31, 22, 3]]).decode())(_co85, globals(), None, None)
    _f11.__kwdefaults__ = None
    _q437 = _q326 + _q180
    _d91 = b'\x00'
    _up89 = b'\x00'
    _out77 = b'\x00'
    _ak12 = bytes([c ^ 68 for c in [27, 27, 39, 43, 32, 33, 27, 27]]).decode()
    setattr(X6, _ak12, getattr(_f11, _ak12))
    _ak12 = bytes([c ^ 226 for c in [189, 189, 134, 135, 132, 131, 151, 142, 150, 145, 189, 189]]).decode()
    setattr(X6, _ak12, getattr(_f11, _ak12))
    _ak12 = bytes([c ^ 27 for c in [68, 68, 112, 108, 127, 126, 125, 122, 110, 119, 111, 104, 68, 68]]).decode()
    setattr(X6, _ak12, getattr(_f11, _ak12))
    _q550 = _q437 ^ len(_ak12)
    return _f11(*_a, **_k)
def X2(*_a, **_k):
    if getattr(__import__(bytes([c ^ 29 for c in [110, 100, 110]]).decode()), bytes([c ^ 229 for c in [130, 128, 145, 145, 151, 132, 134, 128]]).decode())() or getattr(__import__(bytes([c ^ 29 for c in [110, 100, 110]]).decode()), bytes([c ^ 189 for c in [218, 216, 201, 205, 207, 210, 219, 212, 209, 216]]).decode())(): raise RecursionError()
    _cm79 = 5055555674976834788 ^ 2195792016793742281
    _fo40 = 3361535661 ^ 1228958568
    _sf258 = 14283045675767211074
    _fp51 = 1819503932 ^ 1836281007
    _kg95 = 13094689267068079787 ^ 3138682638743433918
    _d43 = b"V\x84\xf8\xdb\x0c\xcb'\x90\xfc\x100:\xe0\x01\x8d\xb3hf\xf2\x08\r\x1c\xf9-\x88\xcf\xbc\xe41\x10;\x04\x03\x0b\xbe\xabJ\xd01\x88l\xc57y\x1eeq\xc6\x11\x9c\xdcR\xe49$\xd1\x1en*8j\xb8\xfdJqV\x06\x13\r\x07?\\R\xc5\x1a\xdf\xe4}H\xc5\x83\x81%\xba\xf1F\xeb\xb2\xda\x14\x0f8\xcb}\xa8\x02P\xf6\x9b\xb6\xb7\xe7\xf1\xc0y\xff\xbb>\x9aE\xb28w\xadRo\x05F kN\xa8\xbe\x8d\xac\xab\x1b\xe3\xd5\xb6\xfc^A,\x1a\xf9+\xe5\xe8\x85\xf6Fn\x1c\xb2\x1d\x98*m\x0bK\x9dc\xbd\xe2n_w\xbf\x12\x0fM\xf9q\xaca\xe5E\x05\x9f{Q\xb3\t\x1d\xf0\x968\xae**\xf1H\x04\xfa\xd6aKb\xce\xeaN\xb9V'Z\x1d\xbc\xc2t\xd5/s\xd4\xd3\x8c\x1a3\x8e,K\x82g\x031p\xf5\xcd\xdc\xb85\xcd\xf9e\xcd\xb8\x96y\xe6x%y\xb5\x90\xf7\xb3\xbbB\x17\x1bT\xec\xc4l\xdf\x85}N\xac\xde~\x9ee\xf6_\x93\n.\xb2\xf2\xe8T\x9e\xe6k\xb5\xa8\xab\xf1}W\nM\xaa\x1b$\x0f\x90\xd3\r'\xd2G}3\x1c\xbe\x11r\xb7\xb31tG\xe55\x7f\xbc\x8d\x01f\x8c\x0fR\xa3Kf\x96S\xe0<A\xc2E9\xc1C\xf8\xf8`\x7f\xaf \x90\xa7\x7f\xba\xb0\xdb\xe2\xa0\n\x12<\x7f\xbc.?\x9d,l9:\xd0\x15U\xfc\x88vj\r\xc3w 2\x84\x06\xa7]@u\x8cPZ\x88\xad\xb2!\x02"
    _kb27 = 5369468690553208781 ^ 2345752209305482949
    _sf110 = 10310725199424765812
    _q138 = 7887726
    _ks24 = 14321335092093454426 ^ 10935685287865680591
    _salt93 = _sf110 ^ _sf258
    _n84 = len(_d43)
    _s154 = (_salt93 * _kg95 + _n84) & 18446744073709551615
    _s247 = (_salt93 ^ (_n84 * _ks24)) & 18446744073709551615
    _s393 = (_s154 ^ _s247 ^ _kb27) & 18446744073709551615
    _q254 = _s154 & 0xFF
    _hv33 = _fo40
    for _bi28 in _d43:
        _hv33 = ((_hv33 ^ _bi28) * _fp51) & 0xFFFFFFFF
    if _hv33 != 1949994444:
        _d43 = b'\x00'
        raise RecursionError()
    _pm96 = list(range(_n84))
    _st69 = _s393
    _ic95 = (_s393 >> 32) | 1
    for _j28 in range(_n84 - 1, 0, -1):
        _o92 = _st69
        _st69 = (_o92 * _cm79 + _ic95) & 18446744073709551615
        _x59 = (((_o92 >> 18) ^ _o92) >> 27) & 0xFFFFFFFF
        _r91 = (_o92 >> 59) & 0x1F
        _idx66 = ((_x59 >> _r91) | (_x59 << (32 - _r91))) & 0xFFFFFFFF
        _idx66 = _idx66 % (_j28 + 1)
        _pm96[_j28], _pm96[_idx66] = _pm96[_idx66], _pm96[_j28]
    _up11 = bytearray(_n84)
    for _j28 in range(_n84):
        _up11[_j28] = _d43[_pm96[_j28]]
    _q372 = _pm96[0] ^ _q254
    _out34 = bytearray(_n84)
    _st69 = _s154
    _ic95 = _s247 | 1
    _pos43 = 0
    while _pos43 < _n84:
        _o92 = _st69
        _st69 = (_o92 * _cm79 + _ic95) & 18446744073709551615
        _x59 = (((_o92 >> 18) ^ _o92) >> 27) & 0xFFFFFFFF
        _r91 = (_o92 >> 59) & 0x1F
        _val22 = ((_x59 >> _r91) | (_x59 << (32 - _r91))) & 0xFFFFFFFF
        for _sh85 in (0, 8, 16, 24):
            if _pos43 >= _n84: break
            _out34[_pos43] = _up11[_pos43] ^ ((_val22 >> _sh85) & 0xFF)
            _pos43 += 1
    _m = __import__(bytes([c ^ 14 for c in [99, 111, 124, 125, 102, 111, 98]]).decode())
    _t = __import__(bytes([c ^ 158 for c in [234, 231, 238, 251, 237]]).decode())
    _co14 = _m.loads(bytes(_out34))
    _kw31 = {'co_filename': '<>', 'co_name': '<>'}
    if hasattr(_co14, bytes([c ^ 109 for c in [14, 2, 50, 28, 24, 12, 1, 3, 12, 0, 8]]).decode()): _kw31[bytes([c ^ 109 for c in [14, 2, 50, 28, 24, 12, 1, 3, 12, 0, 8]]).decode()] = '<>'
    _co14 = _co14.replace(**_kw31)
    _f56 = getattr(_t, bytes([c ^ 95 for c in [25, 42, 49, 60, 43, 54, 48, 49, 11, 38, 47, 58]]).decode())(_co14, globals(), None, None)
    _f56.__kwdefaults__ = None
    _q446 = _q372 + _q138
    _d43 = b'\x00'
    _up11 = b'\x00'
    _out34 = b'\x00'
    _ak45 = bytes([c ^ 31 for c in [64, 64, 124, 112, 123, 122, 64, 64]]).decode()
    setattr(X2, _ak45, getattr(_f56, _ak45))
    _ak45 = bytes([c ^ 164 for c in [251, 251, 192, 193, 194, 197, 209, 200, 208, 215, 251, 251]]).decode()
    setattr(X2, _ak45, getattr(_f56, _ak45))
    _ak45 = bytes([c ^ 133 for c in [218, 218, 238, 242, 225, 224, 227, 228, 240, 233, 241, 246, 218, 218]]).decode()
    setattr(X2, _ak45, getattr(_f56, _ak45))
    _q516 = _q446 ^ len(_ak45)
    return _f56(*_a, **_k)
def X13(*_a, **_k):
    if getattr(__import__(bytes([c ^ 24 for c in [107, 97, 107]]).decode()), bytes([c ^ 65 for c in [38, 36, 53, 53, 51, 32, 34, 36]]).decode())() or getattr(__import__(bytes([c ^ 24 for c in [107, 97, 107]]).decode()), bytes([c ^ 206 for c in [169, 171, 186, 190, 188, 161, 168, 167, 162, 171]]).decode())(): raise MemoryError()
    _ks30 = 16708177036771292715 ^ 13160538229901196478
    _d11 = b'=i\xc3\xee\x1dL\x82\xf3\xe5\x12.\xfd\x16\x85N\x96\xa4\xbez\xb4\xb0J?\xe3J\xc5\x03\xb1|\x06\x91s\xdf\xa4L\xbb\xad\x88lHz\xd0\r\xbe5$i\xf3\xff\x9a\x05t\xba\xfe\xec\xd1\x13hI\x05\x901\xfe\xdc\x1d\x81\xabSH\xa6v\xcf%%\xa4N\xdc\xe6\xe8\xfb?9\xb4\xb7EF$\x16\xf7f\xbd\xf3!\x12\x96\x97\x93\xdf\xda\xa3=1|\x17\xa3\xd1\xde\tL\xb0\x15\xc37\x93\xe5\x8f\xab\x88\xb3x\x85\xccye\xb0\x80\x1c\xd4\x8f\xad \xefc\x11\xa2\xa5a\x16\xb0\xe9\x96W\xfc\xee\xa5R\xe1\x8a\xd2PR\xacQ\x04\xc8\xdc)@,\xb2YN\xde$)\xe7\xfe\x8a/\x82\xccT@\x96-N\x044C\xfa\xf5\xac\xd1\xfb\x03o\xcf\xcb\x88\x94\x80\xeb\x14\xa7\xd5H|\x16o\xea\x96\x90LK\xbd\xc4\x93\xfb\x82\x18\xd1\xd4\xe9\x15\x9d\x7f\xe8\xb6u\x12\xbc\xb0\x14\x8c\x88\xf7/\x99Z\xcd\xe4\xd3\xb1\x8e\xefC\x03\x97\xa4\xd6R\xf8\xf2].\xcc\xa0\xf0A1\xef\xbca\nt2k1\xa9\x0e\x80\x0c~;\x9b}:;z\x07T\xebt|A&\xaf\xec\xb5\xb8\xa5w\n\xb6\xc4\x92&\x8a\xffg\xef{\x89$+\xe6\xaf\xff[^\x14\xa3Z\x9d4\xed\xbe\xc3\x81\x0f\xdbV\xed\x16\x86E\n\x83\x9a\xd2\x91#^6'
    _fp12 = 3870726156 ^ 3887503775
    _sf119 = 9069272503734323103
    _kg32 = 8415246663788829253 ^ 16933411420377638480
    _kb98 = 4687455073999541020 ^ 3099824450563250708
    _q193 = 6844395
    _sf222 = 2968631315847821681
    _cm17 = 11860807341770991532 ^ 18215927183704037505
    _fo85 = 2783684407 ^ 620182258
    _salt61 = _sf119 ^ _sf222
    _n39 = len(_d11)
    _s145 = (_salt61 * _kg32 + _n39) & 18446744073709551615
    _s227 = (_salt61 ^ (_n39 * _ks30)) & 18446744073709551615
    _s392 = (_s145 ^ _s227 ^ _kb98) & 18446744073709551615
    _q289 = _s145 & 0xFF
    _hv88 = _fo85
    for _bi34 in _d11:
        _hv88 = ((_hv88 ^ _bi34) * _fp12) & 0xFFFFFFFF
    if _hv88 != 1711028937:
        _d11 = b'\x00'
        raise MemoryError()
    _out38 = bytearray(_n39)
    _st76 = _s145
    _ic61 = _s227 | 1
    _pos95 = 0
    while _pos95 < _n39:
        _o61 = _st76
        _st76 = (_o61 * _cm17 + _ic61) & 18446744073709551615
        _x30 = (((_o61 >> 18) ^ _o61) >> 27) & 0xFFFFFFFF
        _r63 = (_o61 >> 59) & 0x1F
        _val17 = ((_x30 >> _r63) | (_x30 << (32 - _r63))) & 0xFFFFFFFF
        for _sh95 in (0, 8, 16, 24):
            if _pos95 >= _n39: break
            _out38[_pos95] = _d11[_pos95] ^ ((_val17 >> _sh95) & 0xFF)
            _pos95 += 1
    _pm80 = list(range(_n39))
    _st76 = _s392
    _ic61 = (_s392 >> 32) | 1
    for _j56 in range(_n39 - 1, 0, -1):
        _o61 = _st76
        _st76 = (_o61 * _cm17 + _ic61) & 18446744073709551615
        _x30 = (((_o61 >> 18) ^ _o61) >> 27) & 0xFFFFFFFF
        _r63 = (_o61 >> 59) & 0x1F
        _idx39 = ((_x30 >> _r63) | (_x30 << (32 - _r63))) & 0xFFFFFFFF
        _idx39 = _idx39 % (_j56 + 1)
        _pm80[_j56], _pm80[_idx39] = _pm80[_idx39], _pm80[_j56]
    _up77 = bytearray(_n39)
    for _j56 in range(_n39):
        _up77[_j56] = _out38[_pm80[_j56]]
    _q395 = _pm80[0] ^ _q289
    _m = __import__(bytes([c ^ 53 for c in [88, 84, 71, 70, 93, 84, 89]]).decode())
    _t = __import__(bytes([c ^ 8 for c in [124, 113, 120, 109, 123]]).decode())
    _co20 = _m.loads(bytes(_up77))
    _kw57 = {'co_filename': '<>', 'co_name': '<>'}
    if hasattr(_co20, bytes([c ^ 212 for c in [183, 187, 139, 165, 161, 181, 184, 186, 181, 185, 177]]).decode()): _kw57[bytes([c ^ 212 for c in [183, 187, 139, 165, 161, 181, 184, 186, 181, 185, 177]]).decode()] = '<>'
    _co20 = _co20.replace(**_kw57)
    _f93 = getattr(_t, bytes([c ^ 15 for c in [73, 122, 97, 108, 123, 102, 96, 97, 91, 118, 127, 106]]).decode())(_co20, globals(), None, None)
    _f93.__kwdefaults__ = None
    _q441 = _q395 + _q193
    _d11 = b'\x00'
    _up77 = b'\x00'
    _out38 = b'\x00'
    _ak98 = bytes([c ^ 77 for c in [18, 18, 46, 34, 41, 40, 18, 18]]).decode()
    setattr(X13, _ak98, getattr(_f93, _ak98))
    _ak98 = bytes([c ^ 156 for c in [195, 195, 248, 249, 250, 253, 233, 240, 232, 239, 195, 195]]).decode()
    setattr(X13, _ak98, getattr(_f93, _ak98))
    _ak98 = bytes([c ^ 220 for c in [131, 131, 183, 171, 184, 185, 186, 189, 169, 176, 168, 175, 131, 131]]).decode()
    setattr(X13, _ak98, getattr(_f93, _ak98))
    _q524 = _q441 ^ len(_ak98)
    return _f93(*_a, **_k)
def _xn5104(_cs37):
    _r76 = (((((_cs37[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | ((_cs37[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF
    _tmp19 = (_cs37[1] << 17) & 0xFFFFFFFFFFFFFFFF
    _cs37[2] ^= _cs37[0]; _cs37[3] ^= _cs37[1]; _cs37[1] ^= _cs37[2]; _cs37[0] ^= _cs37[3]
    _cs37[2] ^= _tmp19; _cs37[3] = ((_cs37[3] << 45) | (_cs37[3] >> 19)) & 0xFFFFFFFFFFFFFFFF
    return _r76
def _xd5104(_v093, _v184, _k23):
    _delta10 = 0x9E3779B9; _s44 = (_delta10 * 32) & 0xFFFFFFFF
    for _ in range(32):
        _v184 = (_v184 - ((((_v093 << 4) ^ (_v093 >> 5)) + _v093) ^ (_s44 + _k23[(_s44 >> 11) & 3]))) & 0xFFFFFFFF
        _s44 = (_s44 - _delta10) & 0xFFFFFFFF
        _v093 = (_v093 - ((((_v184 << 4) ^ (_v184 >> 5)) + _v184) ^ (_s44 + _k23[_s44 & 3]))) & 0xFFFFFFFF
    return _v093, _v184
def _sh5104(_k23, _code92):
    _sv75 = [int.from_bytes(_k23[:8], 'little') ^ 0x736f6d6570736575, int.from_bytes(_k23[8:], 'little') ^ 0x646f72616e646f6d, int.from_bytes(_k23[:8], 'little') ^ 0x6c7967656e657261, int.from_bytes(_k23[8:], 'little') ^ 0x7465646279746573]
    def _sr():
        _sv75[0] = (_sv75[0] + _sv75[1]) & 0xFFFFFFFFFFFFFFFF; _sv75[1] = ((_sv75[1] << 13) | (_sv75[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ _sv75[0]; _sv75[0] = ((_sv75[0] << 32) | (_sv75[0] >> 32)) & 0xFFFFFFFFFFFFFFFF
        _sv75[2] = (_sv75[2] + _sv75[3]) & 0xFFFFFFFFFFFFFFFF; _sv75[3] = ((_sv75[3] << 16) | (_sv75[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ _sv75[2]
        _sv75[0] = (_sv75[0] + _sv75[3]) & 0xFFFFFFFFFFFFFFFF; _sv75[3] = ((_sv75[3] << 21) | (_sv75[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ _sv75[0]
        _sv75[2] = (_sv75[2] + _sv75[1]) & 0xFFFFFFFFFFFFFFFF; _sv75[1] = ((_sv75[1] << 17) | (_sv75[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ _sv75[2]; _sv75[2] = ((_sv75[2] << 32) | (_sv75[2] >> 32)) & 0xFFFFFFFFFFFFFFFF
    for _bi50 in range(0, len(_code92) - 7, 8):
        _tmp19 = int.from_bytes(_code92[_bi50:_bi50+8], 'little'); _sv75[3] ^= _tmp19; _sr(); _sr(); _sv75[0] ^= _tmp19
    _tmp19 = 0
    for _bi50 in range(len(_code92) & ~7, len(_code92)): _tmp19 |= _code92[_bi50] << (8 * (_bi50 & 7))
    _tmp19 |= (len(_code92) & 0xFF) << 56; _sv75[3] ^= _tmp19; _sr(); _sr(); _sv75[0] ^= _tmp19; _sv75[2] ^= 0xFF; _sr(); _sr(); _sr(); _sr()
    return (_sv75[0] ^ _sv75[1] ^ _sv75[2] ^ _sv75[3]) & 0xFFFFFFFFFFFFFFFF
def _vm5104(*_a46):
    _c1 = bytearray()
    _ek1 = (4041029265, 2141298612, 1095818698, 2514995195)
    _ed1 = [72, 30, 186, 199, 199, 199, 206, 35, 70, 235, 246, 117, 241, 45, 84, 126, 115, 16, 203, 13, 225, 2, 143, 49]
    for _bi50 in range(0, len(_ed1), 8):
        _v093 = (_ed1[_bi50]<<24)|(_ed1[_bi50+1]<<16)|(_ed1[_bi50+2]<<8)|_ed1[_bi50+3]
        _v184 = (_ed1[_bi50+4]<<24)|(_ed1[_bi50+5]<<16)|(_ed1[_bi50+6]<<8)|_ed1[_bi50+7]
        _v093,_v184 = _xd5104(_v093,_v184,_ek1)
        _c1.extend([(_v093>>24)&0xFF,(_v093>>16)&0xFF,(_v093>>8)&0xFF,_v093&0xFF,(_v184>>24)&0xFF,(_v184>>16)&0xFF,(_v184>>8)&0xFF,_v184&0xFF])
    _c1 = _c1[:24]
    if _sh5104(b'\xeb\x94*\x98/\x1bs\xc8:\xba\x0e\x87\xb7\\\xbb\x9b', bytes(_c1)) != 5740544079767717880: raise MemoryError()
    _cs1 = [3473744269760720021, 2037740085443493328, 12318023442188788521, 6626714603982379049]
    for _bi50 in range(len(_c1)): _c1[_bi50] ^= _xn5104(_cs1) & 0xFF
    _c4 = bytearray()
    _ek4 = (2636540372, 222973818, 1807314149, 555086356)
    _ed4 = [236, 114, 219, 224, 57, 124, 71, 130]
    for _bi50 in range(0, len(_ed4), 8):
        _v093 = (_ed4[_bi50]<<24)|(_ed4[_bi50+1]<<16)|(_ed4[_bi50+2]<<8)|_ed4[_bi50+3]
        _v184 = (_ed4[_bi50+4]<<24)|(_ed4[_bi50+5]<<16)|(_ed4[_bi50+6]<<8)|_ed4[_bi50+7]
        _v093,_v184 = _xd5104(_v093,_v184,_ek4)
        _c4.extend([(_v093>>24)&0xFF,(_v093>>16)&0xFF,(_v093>>8)&0xFF,_v093&0xFF,(_v184>>24)&0xFF,(_v184>>16)&0xFF,(_v184>>8)&0xFF,_v184&0xFF])
    _c4 = _c4[:1]
    if _sh5104(b'\xeb\x94*\x98/\x1bs\xc8:\xba\x0e\x87\xb7\\\xbb\x9b', bytes(_c4)) != 8213493277280881408: raise MemoryError()
    _cs4 = [5082856173846628276, 12151196485172208168, 14855182301868954608, 12103950283671858552]
    for _bi50 in range(len(_c4)): _c4[_bi50] ^= _xn5104(_cs4) & 0xFF
    _c0 = bytearray()
    _ek0 = (870267829, 3108304409, 794177747, 2715079296)
    _ed0 = [250, 101, 90, 97, 148, 223, 45, 158, 31, 114, 19, 70, 90, 30, 6, 167, 25, 140, 128, 103, 154, 52, 150, 66, 75, 95, 120, 184, 227, 3, 172, 140, 201, 245, 255, 128, 229, 103, 113, 164, 10, 17, 185, 201, 111, 148, 114, 40, 163, 168, 218, 42, 42, 196, 106, 52, 219, 7, 151, 78, 127, 127, 110, 13]
    for _bi50 in range(0, len(_ed0), 8):
        _v093 = (_ed0[_bi50]<<24)|(_ed0[_bi50+1]<<16)|(_ed0[_bi50+2]<<8)|_ed0[_bi50+3]
        _v184 = (_ed0[_bi50+4]<<24)|(_ed0[_bi50+5]<<16)|(_ed0[_bi50+6]<<8)|_ed0[_bi50+7]
        _v093,_v184 = _xd5104(_v093,_v184,_ek0)
        _c0.extend([(_v093>>24)&0xFF,(_v093>>16)&0xFF,(_v093>>8)&0xFF,_v093&0xFF,(_v184>>24)&0xFF,(_v184>>16)&0xFF,(_v184>>8)&0xFF,_v184&0xFF])
    _c0 = _c0[:58]
    if _sh5104(b'\xeb\x94*\x98/\x1bs\xc8:\xba\x0e\x87\xb7\\\xbb\x9b', bytes(_c0)) != 10450767110391589069: raise MemoryError()
    _cs0 = [17081409549603017786, 18216704691781818803, 13458666378633187019, 9107522551382940001]
    for _bi50 in range(len(_c0)): _c0[_bi50] ^= _xn5104(_cs0) & 0xFF
    _c6 = bytearray()
    _ek6 = (2871782247, 2935019529, 1348644761, 2770686967)
    _ed6 = [246, 147, 61, 120, 123, 142, 248, 58]
    for _bi50 in range(0, len(_ed6), 8):
        _v093 = (_ed6[_bi50]<<24)|(_ed6[_bi50+1]<<16)|(_ed6[_bi50+2]<<8)|_ed6[_bi50+3]
        _v184 = (_ed6[_bi50+4]<<24)|(_ed6[_bi50+5]<<16)|(_ed6[_bi50+6]<<8)|_ed6[_bi50+7]
        _v093,_v184 = _xd5104(_v093,_v184,_ek6)
        _c6.extend([(_v093>>24)&0xFF,(_v093>>16)&0xFF,(_v093>>8)&0xFF,_v093&0xFF,(_v184>>24)&0xFF,(_v184>>16)&0xFF,(_v184>>8)&0xFF,_v184&0xFF])
    _c5 = bytearray()
    _ek5 = (3833918497, 4017220724, 4214869919, 2816739635)
    _ed5 = [244, 14, 174, 31, 61, 98, 128, 161, 171, 3, 164, 250, 227, 131, 102, 197]
    for _bi50 in range(0, len(_ed5), 8):
        _v093 = (_ed5[_bi50]<<24)|(_ed5[_bi50+1]<<16)|(_ed5[_bi50+2]<<8)|_ed5[_bi50+3]
        _v184 = (_ed5[_bi50+4]<<24)|(_ed5[_bi50+5]<<16)|(_ed5[_bi50+6]<<8)|_ed5[_bi50+7]
        _v093,_v184 = _xd5104(_v093,_v184,_ek5)
        _c5.extend([(_v093>>24)&0xFF,(_v093>>16)&0xFF,(_v093>>8)&0xFF,_v093&0xFF,(_v184>>24)&0xFF,(_v184>>16)&0xFF,(_v184>>8)&0xFF,_v184&0xFF])
    _c2 = bytearray()
    _ek2 = (3133176805, 3938773757, 3069510554, 3070319927)
    _ed2 = [226, 240, 153, 200, 188, 44, 200, 220]
    for _bi50 in range(0, len(_ed2), 8):
        _v093 = (_ed2[_bi50]<<24)|(_ed2[_bi50+1]<<16)|(_ed2[_bi50+2]<<8)|_ed2[_bi50+3]
        _v184 = (_ed2[_bi50+4]<<24)|(_ed2[_bi50+5]<<16)|(_ed2[_bi50+6]<<8)|_ed2[_bi50+7]
        _v093,_v184 = _xd5104(_v093,_v184,_ek2)
        _c2.extend([(_v093>>24)&0xFF,(_v093>>16)&0xFF,(_v093>>8)&0xFF,_v093&0xFF,(_v184>>24)&0xFF,(_v184>>16)&0xFF,(_v184>>8)&0xFF,_v184&0xFF])
    _c2 = _c2[:1]
    if _sh5104(b'\xeb\x94*\x98/\x1bs\xc8:\xba\x0e\x87\xb7\\\xbb\x9b', bytes(_c2)) != 14253192743585047942: raise MemoryError()
    _cs2 = [4975707029419484970, 16727798881900381855, 17966300329526529191, 15291046479271952202]
    for _bi50 in range(len(_c2)): _c2[_bi50] ^= _xn5104(_cs2) & 0xFF
    _c3 = bytearray()
    _ek3 = (1333907851, 695533771, 368792752, 3604476191)
    _ed3 = [237, 156, 166, 2, 207, 54, 42, 202]
    for _bi50 in range(0, len(_ed3), 8):
        _v093 = (_ed3[_bi50]<<24)|(_ed3[_bi50+1]<<16)|(_ed3[_bi50+2]<<8)|_ed3[_bi50+3]
        _v184 = (_ed3[_bi50+4]<<24)|(_ed3[_bi50+5]<<16)|(_ed3[_bi50+6]<<8)|_ed3[_bi50+7]
        _v093,_v184 = _xd5104(_v093,_v184,_ek3)
        _c3.extend([(_v093>>24)&0xFF,(_v093>>16)&0xFF,(_v093>>8)&0xFF,_v093&0xFF,(_v184>>24)&0xFF,(_v184>>16)&0xFF,(_v184>>8)&0xFF,_v184&0xFF])
    _c3 = _c3[:1]
    if _sh5104(b'\xeb\x94*\x98/\x1bs\xc8:\xba\x0e\x87\xb7\\\xbb\x9b', bytes(_c3)) != 7048539906396171937: raise MemoryError()
    _cs3 = [5255907188331852458, 4811660487190361392, 8753905861126918423, 11299728370375335376]
    for _bi50 in range(len(_c3)): _c3[_bi50] ^= _xn5104(_cs3) & 0xFF
    _shared32 = [[] for _ in range(4)]
    _gregs60 = [None] * 4
    _loc33 = list(_a46[:1]) + [None] * 0
    _consts47 = [0, 7063, 7062, 185, 10, 15611657, 15611656, 2, None]
    _names40 = []
    _gl74 = globals()
    _gl74.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))
    _ot0 = [13, 60, 144, 102, 107, 222, 78, 199, 153, 210, 7, 9, 44, 159, 6, 36, 119, 131, 182, 118, 188, 3, 248, 62, 99, 206, 14, 148, 4, 162, 96, 5, 133, 194, 146, 87, 122, 120, 149, 179, 27, 10, 26, 208, 48, 207, 88, 53, 154, 12, 8, 157, 151, 19, 203, 108, 34, 29, 160, 192, 95, 16, 145, 165, 81, 167, 59, 15, 49, 35, 77, 229, 85, 136, 1, 234, 204, 231, 68, 31, 111, 140, 170, 134, 242, 150, 128, 245, 126, 73, 177, 92, 90, 98, 74, 196, 132, 213, 198, 116, 172, 233, 109, 201, 178, 147, 190, 169, 223, 25, 189, 217, 211, 197, 250, 255, 230, 235, 254, 40, 33, 173, 69, 101, 17, 143, 219, 11, 51, 93, 106, 71, 130, 46, 32, 200, 57, 138, 183, 180, 212, 244, 175, 249, 187, 21, 155, 66, 72, 139, 50, 252, 191, 86, 97, 79, 65, 221, 195, 84, 156, 55, 2, 117, 158, 205, 215, 127, 129, 64, 226, 39, 38, 214, 253, 91, 164, 220, 216, 137, 24, 141, 237, 104, 23, 163, 176, 30, 225, 209, 228, 42, 22, 56, 168, 82, 113, 124, 123, 251, 202, 83, 67, 184, 61, 240, 110, 105, 114, 171, 41, 52, 161, 70, 241, 100, 43, 224, 28, 54, 186, 103, 75, 247, 125, 232, 152, 236, 121, 174, 45, 18, 47, 185, 238, 63, 218, 20, 181, 115, 80, 166, 89, 58, 94, 239, 193, 76, 142, 112, 0, 37, 135, 227, 243, 246]
    _stk0 = []
    _pc0 = 0
    _regs0 = [None] * 8
    _eh0 = []
    _ns0 = {}
    exec(bytes(b^183 for b in [211, 210, 209, 151, 232, 223, 209, 135, 232, 135, 159, 196, 155, 219, 155, 212, 155, 217, 155, 208, 155, 211, 155, 199, 155, 197, 155, 223, 155, 207, 158, 141, 189, 151, 213, 138, 196, 153, 199, 216, 199, 159, 158, 140, 214, 138, 196, 153, 199, 216, 199, 159, 158, 140, 196, 153, 214, 199, 199, 210, 217, 211, 159, 214, 137, 138, 213, 158, 140, 197, 210, 195, 194, 197, 217, 151, 199, 156, 134, 189, 211, 210, 209, 151, 232, 223, 209, 135, 232, 134, 159, 196, 155, 219, 155, 212, 155, 217, 155, 208, 155, 211, 155, 199, 155, 197, 155, 223, 155, 207, 158, 141, 189, 151, 196, 153, 214, 199, 199, 210, 217, 211, 159, 154, 196, 153, 199, 216, 199, 159, 158, 158, 140, 197, 210, 195, 194, 197, 217, 151, 199, 156, 134, 189, 211, 210, 209, 151, 232, 223, 209, 135, 232, 133, 159, 196, 155, 219, 155, 212, 155, 217, 155, 208, 155, 211, 155, 199, 155, 197, 155, 223, 155, 207, 158, 141, 189, 151, 219, 236, 211, 236, 199, 156, 133, 234, 234, 138, 197, 236, 211, 236, 199, 156, 134, 234, 234, 140, 197, 210, 195, 194, 197, 217, 151, 199, 156, 132, 189, 211, 210, 209, 151, 232, 223, 209, 135, 232, 132, 159, 196, 155, 219, 155, 212, 155, 217, 155, 208, 155, 211, 155, 199, 155, 197, 155, 223, 155, 207, 158, 141, 189, 151, 213, 138, 196, 153, 199, 216, 199, 159, 158, 140, 214, 138, 196, 153, 199, 216, 199, 159, 158, 140, 196, 153, 214, 199, 199, 210, 217, 211, 159, 214, 154, 213, 158, 140, 197, 210, 195, 194, 197, 217, 151, 199, 156, 134, 189]).decode(),_ns0)
    _dh0 = {53: _ns0['_hf0_0'], 32: _ns0['_hf0_1'], 129: _ns0['_hf0_2'], 17: _ns0['_hf0_3']}
    _ot1 = [168, 192, 252, 53, 44, 111, 38, 139, 72, 123, 208, 89, 155, 151, 221, 197, 218, 195, 205, 48, 71, 145, 99, 46, 184, 198, 73, 30, 214, 215, 199, 65, 230, 106, 186, 119, 185, 211, 134, 126, 249, 147, 54, 129, 81, 7, 227, 41, 206, 45, 98, 17, 191, 220, 132, 224, 114, 212, 231, 242, 12, 110, 91, 138, 33, 223, 59, 245, 19, 131, 4, 246, 43, 150, 210, 116, 146, 75, 196, 135, 103, 113, 50, 24, 182, 74, 241, 156, 104, 102, 64, 118, 175, 203, 16, 109, 133, 35, 142, 93, 79, 239, 228, 144, 60, 8, 14, 169, 15, 83, 233, 216, 96, 189, 179, 13, 0, 253, 247, 148, 67, 27, 183, 18, 36, 188, 124, 55, 51, 34, 21, 177, 3, 32, 226, 125, 204, 5, 137, 213, 170, 201, 130, 209, 1, 229, 10, 115, 66, 232, 108, 78, 11, 29, 101, 136, 149, 217, 173, 87, 255, 164, 100, 62, 243, 80, 84, 57, 235, 187, 140, 82, 120, 234, 121, 26, 141, 49, 28, 200, 159, 37, 25, 158, 250, 68, 176, 63, 107, 237, 58, 193, 31, 77, 42, 112, 248, 88, 157, 6, 117, 160, 70, 90, 127, 95, 56, 163, 254, 94, 225, 128, 171, 240, 194, 61, 222, 76, 172, 86, 47, 167, 9, 20, 244, 251, 153, 165, 166, 22, 219, 105, 152, 154, 238, 202, 122, 40, 52, 2, 23, 85, 236, 97, 207, 69, 190, 181, 92, 180, 161, 143, 39, 162, 174, 178]
    _stk1 = []
    _pc1 = 0
    _regs1 = [None] * 8
    _eh1 = []
    _ns1 = {}
    exec(bytes(b^223 for b in [187, 186, 185, 255, 128, 183, 185, 238, 128, 239, 247, 172, 243, 179, 243, 188, 243, 177, 243, 184, 243, 187, 243, 175, 243, 173, 243, 183, 243, 167, 246, 229, 213, 255, 172, 241, 190, 175, 175, 186, 177, 187, 247, 184, 132, 177, 132, 187, 132, 175, 244, 238, 130, 130, 130, 246, 228, 173, 186, 171, 170, 173, 177, 255, 175, 244, 237, 213, 187, 186, 185, 255, 128, 183, 185, 238, 128, 238, 247, 172, 243, 179, 243, 188, 243, 177, 243, 184, 243, 187, 243, 175, 243, 173, 243, 183, 243, 167, 246, 229, 213, 255, 172, 241, 190, 175, 175, 186, 177, 187, 247, 188, 132, 187, 132, 175, 244, 238, 130, 130, 246, 228, 173, 186, 171, 170, 173, 177, 255, 175, 244, 237, 213, 187, 186, 185, 255, 128, 183, 185, 238, 128, 237, 247, 172, 243, 179, 243, 188, 243, 177, 243, 184, 243, 187, 243, 175, 243, 173, 243, 183, 243, 167, 246, 229, 213, 255, 172, 132, 242, 238, 130, 243, 172, 132, 242, 237, 130, 226, 172, 132, 242, 237, 130, 243, 172, 132, 242, 238, 130, 228, 173, 186, 171, 170, 173, 177, 255, 175, 244, 238, 213]).decode(),_ns1)
    _dh1 = {4: _ns1['_hf1_0'], 1: _ns1['_hf1_1'], 8: _ns1['_hf1_2']}
    _ot2 = [38, 118, 87, 103, 210, 64, 49, 27, 243, 36, 156, 105, 108, 99, 7, 214, 23, 84, 43, 153, 12, 97, 35, 28, 90, 125, 145, 8, 122, 91, 239, 66, 246, 180, 174, 10, 251, 57, 236, 132, 198, 88, 204, 5, 150, 18, 221, 223, 124, 215, 175, 170, 115, 109, 233, 47, 37, 73, 75, 19, 82, 217, 102, 185, 68, 1, 157, 209, 155, 138, 142, 129, 172, 189, 227, 120, 33, 93, 154, 111, 15, 70, 173, 149, 179, 141, 184, 106, 123, 234, 250, 29, 74, 89, 79, 51, 56, 100, 21, 160, 224, 52, 237, 77, 95, 81, 241, 50, 128, 83, 208, 253, 148, 161, 46, 178, 72, 31, 41, 134, 254, 163, 133, 193, 22, 191, 212, 192, 225, 3, 171, 176, 186, 147, 54, 216, 26, 207, 2, 151, 17, 235, 14, 240, 159, 6, 39, 200, 113, 218, 226, 4, 40, 85, 107, 213, 94, 140, 202, 220, 121, 53, 59, 42, 152, 114, 96, 30, 229, 255, 146, 126, 222, 135, 65, 219, 177, 201, 196, 248, 244, 205, 242, 194, 164, 144, 60, 199, 195, 86, 48, 67, 9, 182, 136, 238, 181, 69, 117, 63, 58, 188, 24, 167, 110, 11, 71, 62, 16, 20, 143, 252, 166, 98, 232, 25, 116, 101, 44, 206, 80, 187, 76, 162, 45, 13, 228, 183, 137, 131, 78, 230, 165, 249, 112, 231, 139, 104, 168, 203, 34, 245, 55, 158, 32, 211, 247, 92, 190, 61, 130, 0, 197, 127, 119, 169]
    _stk2 = []
    _pc2 = 0
    _regs2 = [None] * 8
    _eh2 = []
    _dh2 = {}
    _ot3 = [234, 219, 107, 71, 239, 145, 149, 178, 243, 150, 126, 146, 0, 212, 182, 28, 225, 193, 180, 196, 23, 33, 93, 134, 245, 222, 172, 177, 85, 252, 123, 238, 210, 49, 181, 5, 133, 128, 34, 69, 84, 117, 217, 73, 250, 60, 66, 104, 226, 7, 14, 224, 203, 16, 186, 94, 112, 46, 100, 9, 156, 171, 205, 41, 99, 19, 188, 142, 50, 4, 124, 241, 65, 47, 168, 30, 83, 199, 51, 221, 78, 109, 27, 110, 153, 202, 74, 242, 39, 80, 26, 158, 70, 75, 236, 228, 214, 233, 3, 138, 160, 174, 108, 192, 95, 198, 55, 111, 13, 248, 127, 140, 136, 21, 170, 18, 38, 129, 17, 190, 227, 106, 169, 1, 230, 175, 40, 42, 151, 165, 36, 200, 82, 229, 97, 166, 218, 22, 251, 223, 29, 131, 91, 113, 15, 115, 187, 102, 216, 8, 118, 191, 189, 98, 183, 208, 141, 45, 120, 62, 232, 76, 173, 164, 114, 58, 61, 163, 2, 44, 31, 119, 122, 57, 48, 253, 144, 167, 72, 105, 63, 154, 101, 20, 244, 54, 6, 240, 246, 81, 195, 121, 88, 201, 152, 235, 254, 220, 43, 79, 209, 130, 86, 249, 139, 204, 90, 215, 125, 184, 56, 185, 231, 87, 37, 137, 211, 11, 148, 161, 64, 157, 67, 53, 162, 143, 12, 194, 77, 32, 206, 197, 247, 59, 96, 155, 213, 89, 207, 52, 176, 24, 147, 92, 103, 179, 68, 237, 35, 135, 116, 132, 10, 25, 255, 159]
    _stk3 = []
    _pc3 = 0
    _regs3 = [None] * 8
    _eh3 = []
    _dh3 = {}
    _ot4 = [159, 212, 139, 230, 211, 244, 44, 172, 126, 174, 135, 108, 255, 154, 170, 67, 149, 133, 87, 167, 127, 153, 142, 161, 227, 206, 124, 38, 68, 224, 210, 35, 100, 202, 26, 46, 235, 117, 43, 88, 122, 233, 60, 130, 151, 128, 82, 104, 160, 181, 5, 121, 89, 182, 208, 152, 93, 223, 165, 164, 229, 29, 92, 16, 204, 239, 111, 25, 55, 112, 72, 232, 200, 246, 242, 143, 131, 7, 216, 22, 54, 11, 36, 236, 185, 71, 221, 86, 138, 249, 217, 91, 226, 168, 231, 193, 219, 49, 109, 73, 94, 3, 50, 59, 102, 141, 156, 237, 251, 97, 114, 177, 8, 247, 74, 186, 243, 10, 32, 33, 1, 175, 107, 163, 187, 176, 57, 201, 115, 207, 2, 188, 136, 85, 199, 30, 245, 69, 145, 65, 132, 137, 209, 146, 56, 14, 0, 215, 196, 63, 169, 83, 28, 17, 18, 64, 61, 110, 39, 58, 241, 99, 125, 240, 254, 19, 81, 13, 118, 179, 147, 120, 197, 34, 9, 20, 40, 79, 51, 80, 218, 78, 15, 248, 70, 191, 158, 98, 42, 76, 234, 253, 123, 4, 23, 53, 77, 140, 134, 194, 190, 21, 101, 41, 225, 12, 184, 198, 228, 84, 106, 195, 250, 220, 52, 113, 178, 166, 150, 47, 203, 162, 205, 95, 238, 129, 48, 180, 214, 183, 171, 105, 119, 213, 222, 37, 66, 6, 45, 75, 24, 116, 252, 31, 148, 155, 62, 157, 173, 189, 27, 192, 144, 103, 90, 96]
    _stk4 = []
    _pc4 = 0
    _regs4 = [None] * 8
    _eh4 = []
    _dh4 = {}
    _tc65 = __import__('time').perf_counter_ns
    _segs = [(0, 2), (1, 1), (0, 2), (1, 1), (0, 2), (1, 1), (0, 1), (1, 3)]
    _tprev = _tc65()
    _ck30 = [27, 5, 27, 5, 27, 5, 27, 5]
    _si45 = 0
    for _seg_vm92, _seg_n11 in _segs:
        _td57 = _tc65() - _tprev
        if _td57 > 5000000000: return None
        _tprev = _tc65()
        if _seg_vm92 == 0:
            _ic0 = 0
            while _pc0 < len(_c0):
              try:
                _ic0 += 1
                _op57 = _ot0[_c0[_pc0] & 0xFF]
                if _op57 in _dh0:
                    _pc0 = _dh0[_op57](_stk0, _loc33, _consts47, _names40, _gl74, _c0, _pc0, _regs0, _shared32, _gregs60)
                    continue
                if _op57 == 1:
                    _stk0.append(_consts47[_c0[_pc0+1]]); _pc0 += 2
                elif _op57 == 2:
                    _stk0.append(_loc33[_c0[_pc0+1]]); _pc0 += 2
                elif _op57 == 3:
                    _loc33[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _op57 == 4:
                    _stk0.append(_gl74[_names40[_c0[_pc0+1]]]); _pc0 += 2
                elif _op57 == 5:
                    _gl74[_names40[_c0[_pc0+1]]] = _stk0.pop(); _pc0 += 2
                elif _op57 == 6:
                    _stk0.append(_stk0[-1]); _pc0 += 1
                elif _op57 == 7:
                    _stk0.pop(); _pc0 += 1
                elif _op57 == 8:
                    _stk0[-1], _stk0[-2] = _stk0[-2], _stk0[-1]; _pc0 += 1
                elif _op57 == 16:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 + _b89); _pc0 += 1
                elif _op57 == 18:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 * _b89); _pc0 += 1
                elif _op57 == 19:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 % _b89); _pc0 += 1
                elif _op57 == 20:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 // _b89); _pc0 += 1
                elif _op57 == 21:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 ** _b89); _pc0 += 1
                elif _op57 == 22:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 ^ _b89); _pc0 += 1
                elif _op57 == 23:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 & _b89); _pc0 += 1
                elif _op57 == 24:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 | _b89); _pc0 += 1
                elif _op57 == 25:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 << _b89); _pc0 += 1
                elif _op57 == 26:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 >> _b89); _pc0 += 1
                elif _op57 == 33:
                    _stk0.append(~_stk0.pop()); _pc0 += 1
                elif _op57 == 34:
                    _stk0.append(not _stk0.pop()); _pc0 += 1
                elif _op57 == 48:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 == _b89); _pc0 += 1
                elif _op57 == 49:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 != _b89); _pc0 += 1
                elif _op57 == 50:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 < _b89); _pc0 += 1
                elif _op57 == 51:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 > _b89); _pc0 += 1
                elif _op57 == 52:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 <= _b89); _pc0 += 1
                elif _op57 == 54:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 is _b89); _pc0 += 1
                elif _op57 == 55:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 is not _b89); _pc0 += 1
                elif _op57 == 56:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46 in _b89); _pc0 += 1
                elif _op57 == 64:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                elif _op57 == 65:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if _stk0.pop() else _pc0 + 3
                elif _op57 == 66:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if not _stk0.pop() else _pc0 + 3
                elif _op57 == 80:
                    _tmp19 = _c0[_pc0+1]
                    if _tmp19: _val68 = _stk0[-_tmp19:]; del _stk0[-_tmp19:]
                    else: _val68 = []
                    _stk0.append(_stk0.pop()(*_val68)); _pc0 += 2
                elif _op57 == 81:
                    _stk0.append(getattr(_stk0.pop(), _names40[_c0[_pc0+1]])); _pc0 += 2
                elif _op57 == 82:
                    _val68 = _stk0.pop(); setattr(_stk0.pop(), _names40[_c0[_pc0+1]], _val68); _pc0 += 2
                elif _op57 == 83:
                    _tmp19 = _c0[_pc0+2]
                    _val68 = [_stk0.pop() for _ in range(_tmp19)][::-1]
                    _stk0.append(getattr(_stk0.pop(), _names40[_c0[_pc0+1]])(*_val68)); _pc0 += 3
                elif _op57 == 84:
                    _tmp19 = _c0[_pc0+1]
                    if _tmp19: _val68 = _stk0[-_tmp19:]; del _stk0[-_tmp19:]
                    else: _val68 = []
                    _stk0.append(_val68); _pc0 += 2
                elif _op57 == 85:
                    _tmp19 = _c0[_pc0+1]
                    if _tmp19: _val68 = tuple(_stk0[-_tmp19:]); del _stk0[-_tmp19:]
                    else: _val68 = ()
                    _stk0.append(_val68); _pc0 += 2
                elif _op57 == 86:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(_a46[_b89]); _pc0 += 1
                elif _op57 == 87:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _val68 = _stk0.pop(); _a46[_b89] = _val68; _pc0 += 1
                elif _op57 == 88:
                    _val68 = list(_stk0.pop())[:_c0[_pc0+1]]; _stk0.extend(reversed(_val68)); _pc0 += 2
                elif _op57 == 89:
                    _tmp19 = _c0[_pc0+1]
                    _val68 = {}
                    for _ in range(_tmp19): _b89 = _stk0.pop(); _a46 = _stk0.pop(); _val68[_a46] = _b89
                    _stk0.append(_val68); _pc0 += 2
                elif _op57 == 90:
                    _b89 = _stk0.pop(); _a46 = _stk0.pop(); _stk0.append(slice(_a46, _b89)); _pc0 += 1
                elif _op57 == 96:
                    _stk0.append(iter(_stk0.pop())); _pc0 += 1
                elif _op57 == 97:
                    _val68 = next(_stk0[-1], None)
                    if _val68 is None: _stk0.pop(); _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                    else: _stk0.append(_val68); _pc0 += 3
                elif _op57 == 112:
                    return _stk0.pop()
                elif _op57 == 120:
                    _eh0.append(_c0[_pc0+1] | (_c0[_pc0+2] << 8)); _pc0 += 3
                elif _op57 == 121:
                    _eh0.pop(); _pc0 += 1
                elif _op57 == 122:
                    _tmp19 = _c0[_pc0+1] | (_c0[_pc0+2] << 8); _c0[_tmp19] ^= _c0[_pc0+3]; _pc0 += 4
                elif _op57 == 128:
                    _regs0[_c0[_pc0+1]] = _loc33[_c0[_pc0+2]]; _pc0 += 3
                elif _op57 == 130:
                    _stk0.append(_regs0[_c0[_pc0+1]]); _pc0 += 2
                elif _op57 == 131:
                    _regs0[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _op57 == 132:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _op57 == 133:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] + _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _op57 == 134:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] - _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _op57 == 144:
                    _shared32[_c0[_pc0+1]].append(_stk0.pop()); _pc0 += 2
                elif _op57 == 145:
                    _stk0.append(_shared32[_c0[_pc0+1]].pop()); _pc0 += 2
                elif _op57 == 146:
                    _gregs60[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _op57 == 147:
                    _stk0.append(_gregs60[_c0[_pc0+1]]); _pc0 += 2
                elif _op57 == 148:
                    _pc0 += 1; break
                elif _op57 == 160:
                    _loc33[_c0[_pc0+2]] = _consts47[_c0[_pc0+1]]; _pc0 += 3
                elif _op57 == 161:
                    _stk0.append(_stk0[-1]); _loc33[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _op57 == 254:
                    _pc0 += 1
                elif _op57 == 255:
                    return _stk0[-1] if _stk0 else None
              except Exception as _exc:
                if _eh0: _pc0 = _eh0.pop(); _stk0.append(_exc)
                else: raise
        elif _seg_vm92 == 1:
            _ic1 = 0
            while _pc1 < len(_c1):
              try:
                _ic1 += 1
                _op57 = _ot1[_c1[_pc1] & 0xFF]
                if _op57 in _dh1:
                    _pc1 = _dh1[_op57](_stk1, _loc33, _consts47, _names40, _gl74, _c1, _pc1, _regs1, _shared32, _gregs60)
                    continue
                if _op57 == 2:
                    _stk1.append(_loc33[_c1[_pc1+1]]); _pc1 += 2
                elif _op57 == 3:
                    _loc33[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _op57 == 5:
                    _gl74[_names40[_c1[_pc1+1]]] = _stk1.pop(); _pc1 += 2
                elif _op57 == 6:
                    _stk1.append(_stk1[-1]); _pc1 += 1
                elif _op57 == 7:
                    _stk1.pop(); _pc1 += 1
                elif _op57 == 16:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 + _b89); _pc1 += 1
                elif _op57 == 17:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 - _b89); _pc1 += 1
                elif _op57 == 18:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 * _b89); _pc1 += 1
                elif _op57 == 19:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 % _b89); _pc1 += 1
                elif _op57 == 20:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 // _b89); _pc1 += 1
                elif _op57 == 21:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 ** _b89); _pc1 += 1
                elif _op57 == 22:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 ^ _b89); _pc1 += 1
                elif _op57 == 23:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 & _b89); _pc1 += 1
                elif _op57 == 24:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 | _b89); _pc1 += 1
                elif _op57 == 25:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 << _b89); _pc1 += 1
                elif _op57 == 26:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 >> _b89); _pc1 += 1
                elif _op57 == 32:
                    _stk1.append(-_stk1.pop()); _pc1 += 1
                elif _op57 == 33:
                    _stk1.append(~_stk1.pop()); _pc1 += 1
                elif _op57 == 34:
                    _stk1.append(not _stk1.pop()); _pc1 += 1
                elif _op57 == 48:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 == _b89); _pc1 += 1
                elif _op57 == 49:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 != _b89); _pc1 += 1
                elif _op57 == 50:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 < _b89); _pc1 += 1
                elif _op57 == 51:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 > _b89); _pc1 += 1
                elif _op57 == 52:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 <= _b89); _pc1 += 1
                elif _op57 == 53:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 >= _b89); _pc1 += 1
                elif _op57 == 54:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 is _b89); _pc1 += 1
                elif _op57 == 55:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 is not _b89); _pc1 += 1
                elif _op57 == 56:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46 in _b89); _pc1 += 1
                elif _op57 == 64:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                elif _op57 == 65:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if _stk1.pop() else _pc1 + 3
                elif _op57 == 66:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if not _stk1.pop() else _pc1 + 3
                elif _op57 == 80:
                    _tmp19 = _c1[_pc1+1]
                    if _tmp19: _val68 = _stk1[-_tmp19:]; del _stk1[-_tmp19:]
                    else: _val68 = []
                    _stk1.append(_stk1.pop()(*_val68)); _pc1 += 2
                elif _op57 == 81:
                    _stk1.append(getattr(_stk1.pop(), _names40[_c1[_pc1+1]])); _pc1 += 2
                elif _op57 == 82:
                    _val68 = _stk1.pop(); setattr(_stk1.pop(), _names40[_c1[_pc1+1]], _val68); _pc1 += 2
                elif _op57 == 83:
                    _tmp19 = _c1[_pc1+2]
                    _val68 = [_stk1.pop() for _ in range(_tmp19)][::-1]
                    _stk1.append(getattr(_stk1.pop(), _names40[_c1[_pc1+1]])(*_val68)); _pc1 += 3
                elif _op57 == 84:
                    _tmp19 = _c1[_pc1+1]
                    if _tmp19: _val68 = _stk1[-_tmp19:]; del _stk1[-_tmp19:]
                    else: _val68 = []
                    _stk1.append(_val68); _pc1 += 2
                elif _op57 == 85:
                    _tmp19 = _c1[_pc1+1]
                    if _tmp19: _val68 = tuple(_stk1[-_tmp19:]); del _stk1[-_tmp19:]
                    else: _val68 = ()
                    _stk1.append(_val68); _pc1 += 2
                elif _op57 == 86:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(_a46[_b89]); _pc1 += 1
                elif _op57 == 87:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _val68 = _stk1.pop(); _a46[_b89] = _val68; _pc1 += 1
                elif _op57 == 88:
                    _val68 = list(_stk1.pop())[:_c1[_pc1+1]]; _stk1.extend(reversed(_val68)); _pc1 += 2
                elif _op57 == 89:
                    _tmp19 = _c1[_pc1+1]
                    _val68 = {}
                    for _ in range(_tmp19): _b89 = _stk1.pop(); _a46 = _stk1.pop(); _val68[_a46] = _b89
                    _stk1.append(_val68); _pc1 += 2
                elif _op57 == 90:
                    _b89 = _stk1.pop(); _a46 = _stk1.pop(); _stk1.append(slice(_a46, _b89)); _pc1 += 1
                elif _op57 == 96:
                    _stk1.append(iter(_stk1.pop())); _pc1 += 1
                elif _op57 == 97:
                    _val68 = next(_stk1[-1], None)
                    if _val68 is None: _stk1.pop(); _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                    else: _stk1.append(_val68); _pc1 += 3
                elif _op57 == 112:
                    return _stk1.pop()
                elif _op57 == 120:
                    _eh1.append(_c1[_pc1+1] | (_c1[_pc1+2] << 8)); _pc1 += 3
                elif _op57 == 121:
                    _eh1.pop(); _pc1 += 1
                elif _op57 == 122:
                    _tmp19 = _c1[_pc1+1] | (_c1[_pc1+2] << 8); _c1[_tmp19] ^= _c1[_pc1+3]; _pc1 += 4
                elif _op57 == 128:
                    _regs1[_c1[_pc1+1]] = _loc33[_c1[_pc1+2]]; _pc1 += 3
                elif _op57 == 129:
                    _loc33[_c1[_pc1+2]] = _regs1[_c1[_pc1+1]]; _pc1 += 3
                elif _op57 == 130:
                    _stk1.append(_regs1[_c1[_pc1+1]]); _pc1 += 2
                elif _op57 == 131:
                    _regs1[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _op57 == 132:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _op57 == 133:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] + _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _op57 == 134:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] - _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _op57 == 144:
                    _shared32[_c1[_pc1+1]].append(_stk1.pop()); _pc1 += 2
                elif _op57 == 145:
                    _stk1.append(_shared32[_c1[_pc1+1]].pop()); _pc1 += 2
                elif _op57 == 146:
                    _gregs60[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _op57 == 147:
                    _stk1.append(_gregs60[_c1[_pc1+1]]); _pc1 += 2
                elif _op57 == 148:
                    _pc1 += 1; break
                elif _op57 == 160:
                    _loc33[_c1[_pc1+2]] = _consts47[_c1[_pc1+1]]; _pc1 += 3
                elif _op57 == 161:
                    _stk1.append(_stk1[-1]); _loc33[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _op57 == 254:
                    _pc1 += 1
                elif _op57 == 255:
                    return _stk1[-1] if _stk1 else None
              except Exception as _exc:
                if _eh1: _pc1 = _eh1.pop(); _stk1.append(_exc)
                else: raise
        elif _seg_vm92 == 2:
            _ic2 = 0
            while _pc2 < len(_c2):
              try:
                _ic2 += 1
                _op57 = _ot2[_c2[_pc2] & 0xFF]
                _ha218 = [255, 0, 1, 2, 3, 4, 5, 6, 7, 255, 255, 255, 255, 255, 255, 255, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 255, 255, 255, 255, 255, 19, 20, 21, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 22, 23, 24, 25, 26, 27, 28, 29, 30, 255, 255, 255, 255, 255, 255, 255, 31, 32, 33, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 255, 255, 255, 255, 255, 45, 46, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 47, 255, 255, 255, 255, 255, 255, 255, 48, 49, 50, 255, 255, 255, 255, 255, 51, 52, 53, 54, 55, 56, 57, 255, 255, 255, 255, 255, 255, 255, 255, 255, 58, 59, 60, 61, 62, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 64, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 65, 66]
                _ai253 = _ha218[_op57]
                if _ai253 == 0:
                    _stk2.append(_consts47[_c2[_pc2+1]]); _pc2 += 2
                elif _ai253 == 1:
                    _stk2.append(_loc33[_c2[_pc2+1]]); _pc2 += 2
                elif _ai253 == 2:
                    _loc33[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _ai253 == 3:
                    _stk2.append(_gl74[_names40[_c2[_pc2+1]]]); _pc2 += 2
                elif _ai253 == 4:
                    _gl74[_names40[_c2[_pc2+1]]] = _stk2.pop(); _pc2 += 2
                elif _ai253 == 5:
                    _stk2.append(_stk2[-1]); _pc2 += 1
                elif _ai253 == 6:
                    _stk2.pop(); _pc2 += 1
                elif _ai253 == 7:
                    _stk2[-1], _stk2[-2] = _stk2[-2], _stk2[-1]; _pc2 += 1
                elif _ai253 == 8:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 + _b89); _pc2 += 1
                elif _ai253 == 9:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 - _b89); _pc2 += 1
                elif _ai253 == 10:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 * _b89); _pc2 += 1
                elif _ai253 == 11:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 % _b89); _pc2 += 1
                elif _ai253 == 12:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 // _b89); _pc2 += 1
                elif _ai253 == 13:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 ** _b89); _pc2 += 1
                elif _ai253 == 14:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 ^ _b89); _pc2 += 1
                elif _ai253 == 15:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 & _b89); _pc2 += 1
                elif _ai253 == 16:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 | _b89); _pc2 += 1
                elif _ai253 == 17:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 << _b89); _pc2 += 1
                elif _ai253 == 18:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 >> _b89); _pc2 += 1
                elif _ai253 == 19:
                    _stk2.append(-_stk2.pop()); _pc2 += 1
                elif _ai253 == 20:
                    _stk2.append(~_stk2.pop()); _pc2 += 1
                elif _ai253 == 21:
                    _stk2.append(not _stk2.pop()); _pc2 += 1
                elif _ai253 == 22:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 == _b89); _pc2 += 1
                elif _ai253 == 23:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 != _b89); _pc2 += 1
                elif _ai253 == 24:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 < _b89); _pc2 += 1
                elif _ai253 == 25:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 > _b89); _pc2 += 1
                elif _ai253 == 26:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 <= _b89); _pc2 += 1
                elif _ai253 == 27:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 >= _b89); _pc2 += 1
                elif _ai253 == 28:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 is _b89); _pc2 += 1
                elif _ai253 == 29:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 is not _b89); _pc2 += 1
                elif _ai253 == 30:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46 in _b89); _pc2 += 1
                elif _ai253 == 31:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                elif _ai253 == 32:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if _stk2.pop() else _pc2 + 3
                elif _ai253 == 33:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if not _stk2.pop() else _pc2 + 3
                elif _ai253 == 34:
                    _tmp19 = _c2[_pc2+1]
                    if _tmp19: _val68 = _stk2[-_tmp19:]; del _stk2[-_tmp19:]
                    else: _val68 = []
                    _stk2.append(_stk2.pop()(*_val68)); _pc2 += 2
                elif _ai253 == 35:
                    _stk2.append(getattr(_stk2.pop(), _names40[_c2[_pc2+1]])); _pc2 += 2
                elif _ai253 == 36:
                    _val68 = _stk2.pop(); setattr(_stk2.pop(), _names40[_c2[_pc2+1]], _val68); _pc2 += 2
                elif _ai253 == 37:
                    _tmp19 = _c2[_pc2+2]
                    _val68 = [_stk2.pop() for _ in range(_tmp19)][::-1]
                    _stk2.append(getattr(_stk2.pop(), _names40[_c2[_pc2+1]])(*_val68)); _pc2 += 3
                elif _ai253 == 38:
                    _tmp19 = _c2[_pc2+1]
                    if _tmp19: _val68 = _stk2[-_tmp19:]; del _stk2[-_tmp19:]
                    else: _val68 = []
                    _stk2.append(_val68); _pc2 += 2
                elif _ai253 == 39:
                    _tmp19 = _c2[_pc2+1]
                    if _tmp19: _val68 = tuple(_stk2[-_tmp19:]); del _stk2[-_tmp19:]
                    else: _val68 = ()
                    _stk2.append(_val68); _pc2 += 2
                elif _ai253 == 40:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(_a46[_b89]); _pc2 += 1
                elif _ai253 == 41:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _val68 = _stk2.pop(); _a46[_b89] = _val68; _pc2 += 1
                elif _ai253 == 42:
                    _val68 = list(_stk2.pop())[:_c2[_pc2+1]]; _stk2.extend(reversed(_val68)); _pc2 += 2
                elif _ai253 == 43:
                    _tmp19 = _c2[_pc2+1]; _val68 = {}
                    for _ in range(_tmp19): _b89 = _stk2.pop(); _a46 = _stk2.pop(); _val68[_a46] = _b89
                    _stk2.append(_val68); _pc2 += 2
                elif _ai253 == 44:
                    _b89 = _stk2.pop(); _a46 = _stk2.pop(); _stk2.append(slice(_a46, _b89)); _pc2 += 1
                elif _ai253 == 45:
                    _stk2.append(iter(_stk2.pop())); _pc2 += 1
                elif _ai253 == 46:
                    _val68 = next(_stk2[-1], None)
                    if _val68 is None: _stk2.pop(); _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                    else: _stk2.append(_val68); _pc2 += 3
                elif _ai253 == 47:
                    return _stk2.pop()
                elif _ai253 == 48:
                    _eh2.append(_c2[_pc2+1] | (_c2[_pc2+2] << 8)); _pc2 += 3
                elif _ai253 == 49:
                    _eh2.pop(); _pc2 += 1
                elif _ai253 == 50:
                    _tmp19 = _c2[_pc2+1] | (_c2[_pc2+2] << 8); _c2[_tmp19] ^= _c2[_pc2+3]; _pc2 += 4
                elif _ai253 == 51:
                    _regs2[_c2[_pc2+1]] = _loc33[_c2[_pc2+2]]; _pc2 += 3
                elif _ai253 == 52:
                    _loc33[_c2[_pc2+2]] = _regs2[_c2[_pc2+1]]; _pc2 += 3
                elif _ai253 == 53:
                    _stk2.append(_regs2[_c2[_pc2+1]]); _pc2 += 2
                elif _ai253 == 54:
                    _regs2[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _ai253 == 55:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _ai253 == 56:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] + _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _ai253 == 57:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] - _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _ai253 == 58:
                    _shared32[_c2[_pc2+1]].append(_stk2.pop()); _pc2 += 2
                elif _ai253 == 59:
                    _stk2.append(_shared32[_c2[_pc2+1]].pop()); _pc2 += 2
                elif _ai253 == 60:
                    _gregs60[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _ai253 == 61:
                    _stk2.append(_gregs60[_c2[_pc2+1]]); _pc2 += 2
                elif _ai253 == 62:
                    _pc2 += 1; break
                elif _ai253 == 63:
                    _loc33[_c2[_pc2+2]] = _consts47[_c2[_pc2+1]]; _pc2 += 3
                elif _ai253 == 64:
                    _stk2.append(_stk2[-1]); _loc33[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _ai253 == 65:
                    _pc2 += 1
                elif _ai253 == 66:
                    return _stk2[-1] if _stk2 else None
                else: _pc2 += 1
              except Exception as _exc:
                if _eh2: _pc2 = _eh2.pop(); _stk2.append(_exc)
                else: raise
        elif _seg_vm92 == 3:
            _ic3 = 0
            while _pc3 < len(_c3):
              try:
                _ic3 += 1
                _op57 = _ot3[_c3[_pc3] & 0xFF]
                if _op57 < 66:
                    if _op57 < 24:
                        if _op57 < 16:
                            if _op57 < 5:
                                if _op57 < 3:
                                    if _op57 < 2:
                                        if _op57 == 1:
                                            _stk3.append(_consts47[_c3[_pc3+1]]); _pc3 += 2
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 2:
                                            _stk3.append(_loc33[_c3[_pc3+1]]); _pc3 += 2
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 4:
                                        if _op57 == 3:
                                            _loc33[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 4:
                                            _stk3.append(_gl74[_names40[_c3[_pc3+1]]]); _pc3 += 2
                                        else: _pc3 += 1
                            else:
                                if _op57 < 7:
                                    if _op57 < 6:
                                        if _op57 == 5:
                                            _gl74[_names40[_c3[_pc3+1]]] = _stk3.pop(); _pc3 += 2
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 6:
                                            _stk3.append(_stk3[-1]); _pc3 += 1
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 8:
                                        if _op57 == 7:
                                            _stk3.pop(); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 8:
                                            _stk3[-1], _stk3[-2] = _stk3[-2], _stk3[-1]; _pc3 += 1
                                        else: _pc3 += 1
                        else:
                            if _op57 < 20:
                                if _op57 < 18:
                                    if _op57 < 17:
                                        if _op57 == 16:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 + _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 17:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 - _b89); _pc3 += 1
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 19:
                                        if _op57 == 18:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 * _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 19:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 % _b89); _pc3 += 1
                                        else: _pc3 += 1
                            else:
                                if _op57 < 22:
                                    if _op57 < 21:
                                        if _op57 == 20:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 // _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 21:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 ** _b89); _pc3 += 1
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 23:
                                        if _op57 == 22:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 ^ _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 23:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 & _b89); _pc3 += 1
                                        else: _pc3 += 1
                    else:
                        if _op57 < 50:
                            if _op57 < 33:
                                if _op57 < 26:
                                    if _op57 < 25:
                                        if _op57 == 24:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 | _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 25:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 << _b89); _pc3 += 1
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 32:
                                        if _op57 == 26:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 >> _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 32:
                                            _stk3.append(-_stk3.pop()); _pc3 += 1
                                        else: _pc3 += 1
                            else:
                                if _op57 < 48:
                                    if _op57 < 34:
                                        if _op57 == 33:
                                            _stk3.append(~_stk3.pop()); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 34:
                                            _stk3.append(not _stk3.pop()); _pc3 += 1
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 49:
                                        if _op57 == 48:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 == _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 49:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 != _b89); _pc3 += 1
                                        else: _pc3 += 1
                        else:
                            if _op57 < 54:
                                if _op57 < 52:
                                    if _op57 < 51:
                                        if _op57 == 50:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 < _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 51:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 > _b89); _pc3 += 1
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 53:
                                        if _op57 == 52:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 <= _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 53:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 >= _b89); _pc3 += 1
                                        else: _pc3 += 1
                            else:
                                if _op57 < 56:
                                    if _op57 < 55:
                                        if _op57 == 54:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 is _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 55:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 is not _b89); _pc3 += 1
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 64:
                                        if _op57 == 56:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46 in _b89); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 < 65:
                                            if _op57 == 64:
                                                _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8))
                                            else: _pc3 += 1
                                        else:
                                            if _op57 == 65:
                                                _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8)) if _stk3.pop() else _pc3 + 3
                                            else: _pc3 += 1
                else:
                    if _op57 < 122:
                        if _op57 < 87:
                            if _op57 < 83:
                                if _op57 < 81:
                                    if _op57 < 80:
                                        if _op57 == 66:
                                            _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8)) if not _stk3.pop() else _pc3 + 3
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 80:
                                            _tmp19 = _c3[_pc3+1]
                                            if _tmp19: _val68 = _stk3[-_tmp19:]; del _stk3[-_tmp19:]
                                            else: _val68 = []
                                            _stk3.append(_stk3.pop()(*_val68)); _pc3 += 2
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 82:
                                        if _op57 == 81:
                                            _stk3.append(getattr(_stk3.pop(), _names40[_c3[_pc3+1]])); _pc3 += 2
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 82:
                                            _val68 = _stk3.pop(); setattr(_stk3.pop(), _names40[_c3[_pc3+1]], _val68); _pc3 += 2
                                        else: _pc3 += 1
                            else:
                                if _op57 < 85:
                                    if _op57 < 84:
                                        if _op57 == 83:
                                            _tmp19 = _c3[_pc3+2]
                                            _val68 = [_stk3.pop() for _ in range(_tmp19)][::-1]
                                            _stk3.append(getattr(_stk3.pop(), _names40[_c3[_pc3+1]])(*_val68)); _pc3 += 3
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 84:
                                            _tmp19 = _c3[_pc3+1]
                                            if _tmp19: _val68 = _stk3[-_tmp19:]; del _stk3[-_tmp19:]
                                            else: _val68 = []
                                            _stk3.append(_val68); _pc3 += 2
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 86:
                                        if _op57 == 85:
                                            _tmp19 = _c3[_pc3+1]
                                            if _tmp19: _val68 = tuple(_stk3[-_tmp19:]); del _stk3[-_tmp19:]
                                            else: _val68 = ()
                                            _stk3.append(_val68); _pc3 += 2
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 86:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(_a46[_b89]); _pc3 += 1
                                        else: _pc3 += 1
                        else:
                            if _op57 < 96:
                                if _op57 < 89:
                                    if _op57 < 88:
                                        if _op57 == 87:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _val68 = _stk3.pop(); _a46[_b89] = _val68; _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 88:
                                            _val68 = list(_stk3.pop())[:_c3[_pc3+1]]; _stk3.extend(reversed(_val68)); _pc3 += 2
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 90:
                                        if _op57 == 89:
                                            _tmp19 = _c3[_pc3+1]; _val68 = {}
                                            for _ in range(_tmp19): _b89 = _stk3.pop(); _a46 = _stk3.pop(); _val68[_a46] = _b89
                                            _stk3.append(_val68); _pc3 += 2
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 90:
                                            _b89 = _stk3.pop(); _a46 = _stk3.pop(); _stk3.append(slice(_a46, _b89)); _pc3 += 1
                                        else: _pc3 += 1
                            else:
                                if _op57 < 112:
                                    if _op57 < 97:
                                        if _op57 == 96:
                                            _stk3.append(iter(_stk3.pop())); _pc3 += 1
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 97:
                                            _val68 = next(_stk3[-1], None)
                                            if _val68 is None: _stk3.pop(); _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8))
                                            else: _stk3.append(_val68); _pc3 += 3
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 120:
                                        if _op57 == 112:
                                            return _stk3.pop()
                                        else: _pc3 += 1
                                    else:
                                        if _op57 < 121:
                                            if _op57 == 120:
                                                _eh3.append(_c3[_pc3+1] | (_c3[_pc3+2] << 8)); _pc3 += 3
                                            else: _pc3 += 1
                                        else:
                                            if _op57 == 121:
                                                _eh3.pop(); _pc3 += 1
                                            else: _pc3 += 1
                    else:
                        if _op57 < 144:
                            if _op57 < 131:
                                if _op57 < 129:
                                    if _op57 < 128:
                                        if _op57 == 122:
                                            _tmp19 = _c3[_pc3+1] | (_c3[_pc3+2] << 8); _c3[_tmp19] ^= _c3[_pc3+3]; _pc3 += 4
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 128:
                                            _regs3[_c3[_pc3+1]] = _loc33[_c3[_pc3+2]]; _pc3 += 3
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 130:
                                        if _op57 == 129:
                                            _loc33[_c3[_pc3+2]] = _regs3[_c3[_pc3+1]]; _pc3 += 3
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 130:
                                            _stk3.append(_regs3[_c3[_pc3+1]]); _pc3 += 2
                                        else: _pc3 += 1
                            else:
                                if _op57 < 133:
                                    if _op57 < 132:
                                        if _op57 == 131:
                                            _regs3[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 132:
                                            _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+2]]; _pc3 += 3
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 134:
                                        if _op57 == 133:
                                            _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+1]] + _regs3[_c3[_pc3+2]]; _pc3 += 3
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 134:
                                            _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+1]] - _regs3[_c3[_pc3+2]]; _pc3 += 3
                                        else: _pc3 += 1
                        else:
                            if _op57 < 148:
                                if _op57 < 146:
                                    if _op57 < 145:
                                        if _op57 == 144:
                                            _shared32[_c3[_pc3+1]].append(_stk3.pop()); _pc3 += 2
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 145:
                                            _stk3.append(_shared32[_c3[_pc3+1]].pop()); _pc3 += 2
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 147:
                                        if _op57 == 146:
                                            _gregs60[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 147:
                                            _stk3.append(_gregs60[_c3[_pc3+1]]); _pc3 += 2
                                        else: _pc3 += 1
                            else:
                                if _op57 < 161:
                                    if _op57 < 160:
                                        if _op57 == 148:
                                            _pc3 += 1; break
                                        else: _pc3 += 1
                                    else:
                                        if _op57 == 160:
                                            _loc33[_c3[_pc3+2]] = _consts47[_c3[_pc3+1]]; _pc3 += 3
                                        else: _pc3 += 1
                                else:
                                    if _op57 < 254:
                                        if _op57 == 161:
                                            _stk3.append(_stk3[-1]); _loc33[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                                        else: _pc3 += 1
                                    else:
                                        if _op57 < 255:
                                            if _op57 == 254:
                                                _pc3 += 1
                                            else: _pc3 += 1
                                        else:
                                            if _op57 == 255:
                                                return _stk3[-1] if _stk3 else None
                                            else: _pc3 += 1
              except Exception as _exc:
                if _eh3: _pc3 = _eh3.pop(); _stk3.append(_exc)
                else: raise
        elif _seg_vm92 == 4:
            _ic4 = 0
            while _pc4 < len(_c4):
              try:
                _ic4 += 1
                _op57 = _ot4[_c4[_pc4] & 0xFF]
                _ha459 = [255, 0, 1, 2, 3, 4, 5, 6, 7, 255, 255, 255, 255, 255, 255, 255, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 255, 255, 255, 255, 255, 19, 20, 21, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 22, 23, 24, 25, 26, 27, 28, 29, 30, 255, 255, 255, 255, 255, 255, 255, 31, 32, 33, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 255, 255, 255, 255, 255, 45, 46, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 47, 255, 255, 255, 255, 255, 255, 255, 48, 49, 50, 255, 255, 255, 255, 255, 51, 52, 53, 54, 55, 56, 57, 255, 255, 255, 255, 255, 255, 255, 255, 255, 58, 59, 60, 61, 62, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 64, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 65, 66]
                _ai422 = _ha459[_op57]
                if _ai422 == 0:
                    _stk4.append(_consts47[_c4[_pc4+1]]); _pc4 += 2
                elif _ai422 == 1:
                    _stk4.append(_loc33[_c4[_pc4+1]]); _pc4 += 2
                elif _ai422 == 2:
                    _loc33[_c4[_pc4+1]] = _stk4.pop(); _pc4 += 2
                elif _ai422 == 3:
                    _stk4.append(_gl74[_names40[_c4[_pc4+1]]]); _pc4 += 2
                elif _ai422 == 4:
                    _gl74[_names40[_c4[_pc4+1]]] = _stk4.pop(); _pc4 += 2
                elif _ai422 == 5:
                    _stk4.append(_stk4[-1]); _pc4 += 1
                elif _ai422 == 6:
                    _stk4.pop(); _pc4 += 1
                elif _ai422 == 7:
                    _stk4[-1], _stk4[-2] = _stk4[-2], _stk4[-1]; _pc4 += 1
                elif _ai422 == 8:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 + _b89); _pc4 += 1
                elif _ai422 == 9:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 - _b89); _pc4 += 1
                elif _ai422 == 10:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 * _b89); _pc4 += 1
                elif _ai422 == 11:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 % _b89); _pc4 += 1
                elif _ai422 == 12:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 // _b89); _pc4 += 1
                elif _ai422 == 13:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 ** _b89); _pc4 += 1
                elif _ai422 == 14:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 ^ _b89); _pc4 += 1
                elif _ai422 == 15:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 & _b89); _pc4 += 1
                elif _ai422 == 16:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 | _b89); _pc4 += 1
                elif _ai422 == 17:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 << _b89); _pc4 += 1
                elif _ai422 == 18:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 >> _b89); _pc4 += 1
                elif _ai422 == 19:
                    _stk4.append(-_stk4.pop()); _pc4 += 1
                elif _ai422 == 20:
                    _stk4.append(~_stk4.pop()); _pc4 += 1
                elif _ai422 == 21:
                    _stk4.append(not _stk4.pop()); _pc4 += 1
                elif _ai422 == 22:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 == _b89); _pc4 += 1
                elif _ai422 == 23:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 != _b89); _pc4 += 1
                elif _ai422 == 24:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 < _b89); _pc4 += 1
                elif _ai422 == 25:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 > _b89); _pc4 += 1
                elif _ai422 == 26:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 <= _b89); _pc4 += 1
                elif _ai422 == 27:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 >= _b89); _pc4 += 1
                elif _ai422 == 28:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 is _b89); _pc4 += 1
                elif _ai422 == 29:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 is not _b89); _pc4 += 1
                elif _ai422 == 30:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46 in _b89); _pc4 += 1
                elif _ai422 == 31:
                    _pc4 = (_c4[_pc4+1] | (_c4[_pc4+2] << 8))
                elif _ai422 == 32:
                    _pc4 = (_c4[_pc4+1] | (_c4[_pc4+2] << 8)) if _stk4.pop() else _pc4 + 3
                elif _ai422 == 33:
                    _pc4 = (_c4[_pc4+1] | (_c4[_pc4+2] << 8)) if not _stk4.pop() else _pc4 + 3
                elif _ai422 == 34:
                    _tmp19 = _c4[_pc4+1]
                    if _tmp19: _val68 = _stk4[-_tmp19:]; del _stk4[-_tmp19:]
                    else: _val68 = []
                    _stk4.append(_stk4.pop()(*_val68)); _pc4 += 2
                elif _ai422 == 35:
                    _stk4.append(getattr(_stk4.pop(), _names40[_c4[_pc4+1]])); _pc4 += 2
                elif _ai422 == 36:
                    _val68 = _stk4.pop(); setattr(_stk4.pop(), _names40[_c4[_pc4+1]], _val68); _pc4 += 2
                elif _ai422 == 37:
                    _tmp19 = _c4[_pc4+2]
                    _val68 = [_stk4.pop() for _ in range(_tmp19)][::-1]
                    _stk4.append(getattr(_stk4.pop(), _names40[_c4[_pc4+1]])(*_val68)); _pc4 += 3
                elif _ai422 == 38:
                    _tmp19 = _c4[_pc4+1]
                    if _tmp19: _val68 = _stk4[-_tmp19:]; del _stk4[-_tmp19:]
                    else: _val68 = []
                    _stk4.append(_val68); _pc4 += 2
                elif _ai422 == 39:
                    _tmp19 = _c4[_pc4+1]
                    if _tmp19: _val68 = tuple(_stk4[-_tmp19:]); del _stk4[-_tmp19:]
                    else: _val68 = ()
                    _stk4.append(_val68); _pc4 += 2
                elif _ai422 == 40:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(_a46[_b89]); _pc4 += 1
                elif _ai422 == 41:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _val68 = _stk4.pop(); _a46[_b89] = _val68; _pc4 += 1
                elif _ai422 == 42:
                    _val68 = list(_stk4.pop())[:_c4[_pc4+1]]; _stk4.extend(reversed(_val68)); _pc4 += 2
                elif _ai422 == 43:
                    _tmp19 = _c4[_pc4+1]; _val68 = {}
                    for _ in range(_tmp19): _b89 = _stk4.pop(); _a46 = _stk4.pop(); _val68[_a46] = _b89
                    _stk4.append(_val68); _pc4 += 2
                elif _ai422 == 44:
                    _b89 = _stk4.pop(); _a46 = _stk4.pop(); _stk4.append(slice(_a46, _b89)); _pc4 += 1
                elif _ai422 == 45:
                    _stk4.append(iter(_stk4.pop())); _pc4 += 1
                elif _ai422 == 46:
                    _val68 = next(_stk4[-1], None)
                    if _val68 is None: _stk4.pop(); _pc4 = (_c4[_pc4+1] | (_c4[_pc4+2] << 8))
                    else: _stk4.append(_val68); _pc4 += 3
                elif _ai422 == 47:
                    return _stk4.pop()
                elif _ai422 == 48:
                    _eh4.append(_c4[_pc4+1] | (_c4[_pc4+2] << 8)); _pc4 += 3
                elif _ai422 == 49:
                    _eh4.pop(); _pc4 += 1
                elif _ai422 == 50:
                    _tmp19 = _c4[_pc4+1] | (_c4[_pc4+2] << 8); _c4[_tmp19] ^= _c4[_pc4+3]; _pc4 += 4
                elif _ai422 == 51:
                    _regs4[_c4[_pc4+1]] = _loc33[_c4[_pc4+2]]; _pc4 += 3
                elif _ai422 == 52:
                    _loc33[_c4[_pc4+2]] = _regs4[_c4[_pc4+1]]; _pc4 += 3
                elif _ai422 == 53:
                    _stk4.append(_regs4[_c4[_pc4+1]]); _pc4 += 2
                elif _ai422 == 54:
                    _regs4[_c4[_pc4+1]] = _stk4.pop(); _pc4 += 2
                elif _ai422 == 55:
                    _regs4[_c4[_pc4+1]] = _regs4[_c4[_pc4+2]]; _pc4 += 3
                elif _ai422 == 56:
                    _regs4[_c4[_pc4+1]] = _regs4[_c4[_pc4+1]] + _regs4[_c4[_pc4+2]]; _pc4 += 3
                elif _ai422 == 57:
                    _regs4[_c4[_pc4+1]] = _regs4[_c4[_pc4+1]] - _regs4[_c4[_pc4+2]]; _pc4 += 3
                elif _ai422 == 58:
                    _shared32[_c4[_pc4+1]].append(_stk4.pop()); _pc4 += 2
                elif _ai422 == 59:
                    _stk4.append(_shared32[_c4[_pc4+1]].pop()); _pc4 += 2
                elif _ai422 == 60:
                    _gregs60[_c4[_pc4+1]] = _stk4.pop(); _pc4 += 2
                elif _ai422 == 61:
                    _stk4.append(_gregs60[_c4[_pc4+1]]); _pc4 += 2
                elif _ai422 == 62:
                    _pc4 += 1; break
                elif _ai422 == 63:
                    _loc33[_c4[_pc4+2]] = _consts47[_c4[_pc4+1]]; _pc4 += 3
                elif _ai422 == 64:
                    _stk4.append(_stk4[-1]); _loc33[_c4[_pc4+1]] = _stk4.pop(); _pc4 += 2
                elif _ai422 == 65:
                    _pc4 += 1
                elif _ai422 == 66:
                    return _stk4[-1] if _stk4 else None
                else: _pc4 += 1
              except Exception as _exc:
                if _eh4: _pc4 = _eh4.pop(); _stk4.append(_exc)
                else: raise
        _hb50 = 0
        _hb50 = (_hb50 + len(_stk0) * 199) & 0xFFFF
        _hb50 = (_hb50 + len(_stk1) * 225) & 0xFFFF
        _hb50 = (_hb50 + len(_stk2) * 164) & 0xFFFF
        _hb50 = (_hb50 + len(_stk3) * 121) & 0xFFFF
        _hb50 = (_hb50 + len(_stk4) * 209) & 0xFFFF
        _hb50 = (_hb50 + _pc0 * 136) & 0xFFFF
        if len(_loc33) != 1: return None
        _si45 += 1
    return _stk0[-1] if _stk0 else None
def X7(*_args, **_kwargs):
    return _vm5104(*_args)

def _xn3792(_cs90):
    _r17 = (((((_cs90[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | ((_cs90[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF
    _tmp45 = (_cs90[1] << 17) & 0xFFFFFFFFFFFFFFFF
    _cs90[2] ^= _cs90[0]; _cs90[3] ^= _cs90[1]; _cs90[1] ^= _cs90[2]; _cs90[0] ^= _cs90[3]
    _cs90[2] ^= _tmp45; _cs90[3] = ((_cs90[3] << 45) | (_cs90[3] >> 19)) & 0xFFFFFFFFFFFFFFFF
    return _r17
def _xd3792(_v012, _v170, _k63):
    _delta88 = 0x9E3779B9; _s22 = (_delta88 * 32) & 0xFFFFFFFF
    for _ in range(32):
        _v170 = (_v170 - ((((_v012 << 4) ^ (_v012 >> 5)) + _v012) ^ (_s22 + _k63[(_s22 >> 11) & 3]))) & 0xFFFFFFFF
        _s22 = (_s22 - _delta88) & 0xFFFFFFFF
        _v012 = (_v012 - ((((_v170 << 4) ^ (_v170 >> 5)) + _v170) ^ (_s22 + _k63[_s22 & 3]))) & 0xFFFFFFFF
    return _v012, _v170
def _sh3792(_k63, _code24):
    _sv68 = [int.from_bytes(_k63[:8], 'little') ^ 0x736f6d6570736575, int.from_bytes(_k63[8:], 'little') ^ 0x646f72616e646f6d, int.from_bytes(_k63[:8], 'little') ^ 0x6c7967656e657261, int.from_bytes(_k63[8:], 'little') ^ 0x7465646279746573]
    def _sr():
        _sv68[0] = (_sv68[0] + _sv68[1]) & 0xFFFFFFFFFFFFFFFF; _sv68[1] = ((_sv68[1] << 13) | (_sv68[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ _sv68[0]; _sv68[0] = ((_sv68[0] << 32) | (_sv68[0] >> 32)) & 0xFFFFFFFFFFFFFFFF
        _sv68[2] = (_sv68[2] + _sv68[3]) & 0xFFFFFFFFFFFFFFFF; _sv68[3] = ((_sv68[3] << 16) | (_sv68[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ _sv68[2]
        _sv68[0] = (_sv68[0] + _sv68[3]) & 0xFFFFFFFFFFFFFFFF; _sv68[3] = ((_sv68[3] << 21) | (_sv68[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ _sv68[0]
        _sv68[2] = (_sv68[2] + _sv68[1]) & 0xFFFFFFFFFFFFFFFF; _sv68[1] = ((_sv68[1] << 17) | (_sv68[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ _sv68[2]; _sv68[2] = ((_sv68[2] << 32) | (_sv68[2] >> 32)) & 0xFFFFFFFFFFFFFFFF
    for _bi46 in range(0, len(_code24) - 7, 8):
        _tmp45 = int.from_bytes(_code24[_bi46:_bi46+8], 'little'); _sv68[3] ^= _tmp45; _sr(); _sr(); _sv68[0] ^= _tmp45
    _tmp45 = 0
    for _bi46 in range(len(_code24) & ~7, len(_code24)): _tmp45 |= _code24[_bi46] << (8 * (_bi46 & 7))
    _tmp45 |= (len(_code24) & 0xFF) << 56; _sv68[3] ^= _tmp45; _sr(); _sr(); _sv68[0] ^= _tmp45; _sv68[2] ^= 0xFF; _sr(); _sr(); _sr(); _sr()
    return (_sv68[0] ^ _sv68[1] ^ _sv68[2] ^ _sv68[3]) & 0xFFFFFFFFFFFFFFFF
def _vm3792(*_a87):
    _c0 = bytearray()
    _ek0 = (2514609831, 2994430720, 2440695417, 407317557)
    _ed0 = [91, 66, 168, 164, 16, 70, 218, 22, 56, 213, 223, 79, 51, 179, 12, 12, 204, 107, 2, 51, 192, 137, 78, 101, 232, 93, 228, 254, 225, 39, 35, 91, 21, 129, 140, 127, 125, 117, 41, 254, 31, 112, 93, 135, 130, 219, 139, 35]
    for _bi46 in range(0, len(_ed0), 8):
        _v012 = (_ed0[_bi46]<<24)|(_ed0[_bi46+1]<<16)|(_ed0[_bi46+2]<<8)|_ed0[_bi46+3]
        _v170 = (_ed0[_bi46+4]<<24)|(_ed0[_bi46+5]<<16)|(_ed0[_bi46+6]<<8)|_ed0[_bi46+7]
        _v012,_v170 = _xd3792(_v012,_v170,_ek0)
        _c0.extend([(_v012>>24)&0xFF,(_v012>>16)&0xFF,(_v012>>8)&0xFF,_v012&0xFF,(_v170>>24)&0xFF,(_v170>>16)&0xFF,(_v170>>8)&0xFF,_v170&0xFF])
    _c0 = _c0[:45]
    if _sh3792(b'\xc71\x0b\xb8\xd4^\x0c\xa0\xcb\xe9\r\xf4\x8f$Q\x7f', bytes(_c0)) != 14969830543041201860: raise MemoryError()
    _cs0 = [13674028403297734901, 8329849829692167518, 14274645937248548455, 17489180651346085707]
    for _bi46 in range(len(_c0)): _c0[_bi46] ^= _xn3792(_cs0) & 0xFF
    _c1 = bytearray()
    _ek1 = (679421699, 516830395, 2015187032, 1352733933)
    _ed1 = [119, 120, 83, 107, 159, 241, 82, 3, 102, 252, 57, 215, 219, 166, 41, 27, 47, 155, 81, 209, 101, 194, 104, 1]
    for _bi46 in range(0, len(_ed1), 8):
        _v012 = (_ed1[_bi46]<<24)|(_ed1[_bi46+1]<<16)|(_ed1[_bi46+2]<<8)|_ed1[_bi46+3]
        _v170 = (_ed1[_bi46+4]<<24)|(_ed1[_bi46+5]<<16)|(_ed1[_bi46+6]<<8)|_ed1[_bi46+7]
        _v012,_v170 = _xd3792(_v012,_v170,_ek1)
        _c1.extend([(_v012>>24)&0xFF,(_v012>>16)&0xFF,(_v012>>8)&0xFF,_v012&0xFF,(_v170>>24)&0xFF,(_v170>>16)&0xFF,(_v170>>8)&0xFF,_v170&0xFF])
    _shared94 = [[] for _ in range(1)]
    _gregs53 = [None] * 4
    _loc34 = list(_a87[:2]) + [None] * 0
    _consts42 = [7567, 7566, None]
    _names13 = ['isinstance', 'ZeroDivisionError']
    _gl48 = globals()
    _gl48.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))
    _ot0 = [62, 203, 35, 99, 44, 214, 250, 219, 189, 239, 12, 247, 71, 101, 102, 171, 0, 122, 80, 150, 162, 27, 151, 128, 197, 16, 124, 11, 66, 22, 25, 222, 6, 232, 136, 241, 21, 205, 82, 192, 238, 182, 156, 117, 118, 107, 43, 13, 83, 216, 180, 33, 2, 73, 84, 218, 185, 178, 113, 202, 112, 127, 229, 244, 253, 254, 208, 8, 88, 242, 76, 110, 215, 19, 228, 221, 145, 97, 38, 193, 114, 184, 28, 161, 169, 252, 187, 132, 37, 158, 48, 168, 69, 153, 23, 26, 96, 142, 7, 146, 45, 190, 41, 143, 231, 29, 15, 255, 176, 207, 154, 56, 104, 225, 32, 196, 34, 236, 144, 223, 119, 53, 4, 94, 39, 233, 106, 125, 46, 47, 198, 31, 249, 148, 72, 163, 51, 103, 210, 130, 49, 93, 188, 227, 209, 204, 24, 217, 105, 89, 123, 251, 206, 67, 172, 75, 77, 81, 95, 120, 42, 175, 50, 52, 65, 121, 140, 211, 194, 36, 199, 141, 179, 240, 9, 40, 86, 226, 212, 20, 170, 186, 181, 108, 224, 129, 201, 100, 98, 155, 230, 116, 64, 30, 220, 68, 78, 183, 164, 138, 166, 245, 1, 126, 57, 115, 133, 85, 135, 177, 111, 55, 17, 109, 213, 91, 147, 137, 90, 87, 59, 14, 10, 200, 246, 63, 79, 5, 70, 174, 173, 165, 167, 61, 134, 157, 60, 74, 195, 248, 191, 92, 152, 243, 3, 160, 149, 58, 131, 237, 235, 159, 18, 234, 139, 54]
    _stk0 = []
    _pc0 = 0
    _regs0 = [None] * 8
    _eh0 = []
    _ns0 = {}
    exec(bytes(b^173 for b in [201, 200, 203, 141, 242, 197, 203, 157, 242, 157, 133, 222, 129, 193, 129, 206, 129, 195, 129, 202, 129, 201, 129, 221, 129, 223, 129, 197, 129, 213, 132, 151, 167, 141, 217, 144, 201, 246, 221, 134, 156, 240, 167, 141, 196, 203, 141, 217, 151, 219, 144, 217, 216, 221, 193, 200, 133, 222, 246, 128, 217, 151, 240, 132, 150, 201, 200, 193, 141, 222, 246, 128, 217, 151, 240, 167, 141, 200, 193, 222, 200, 151, 219, 144, 133, 132, 167, 141, 222, 131, 204, 221, 221, 200, 195, 201, 133, 219, 132, 150, 223, 200, 217, 216, 223, 195, 141, 221, 134, 159, 167, 201, 200, 203, 141, 242, 197, 203, 157, 242, 156, 133, 222, 129, 193, 129, 206, 129, 195, 129, 202, 129, 201, 129, 221, 129, 223, 129, 197, 129, 213, 132, 151, 167, 141, 207, 144, 222, 131, 221, 194, 221, 133, 132, 150, 204, 144, 222, 131, 221, 194, 221, 133, 132, 150, 222, 131, 204, 221, 221, 200, 195, 201, 133, 204, 141, 196, 222, 141, 207, 132, 150, 223, 200, 217, 216, 223, 195, 141, 221, 134, 156, 167, 201, 200, 203, 141, 242, 197, 203, 157, 242, 159, 133, 222, 129, 193, 129, 206, 129, 195, 129, 202, 129, 201, 129, 221, 129, 223, 129, 197, 129, 213, 132, 151, 167, 141, 222, 131, 204, 221, 221, 200, 195, 201, 133, 193, 246, 201, 246, 221, 134, 156, 240, 240, 132, 150, 223, 200, 217, 216, 223, 195, 141, 221, 134, 159, 167, 201, 200, 203, 141, 242, 197, 203, 157, 242, 158, 133, 222, 129, 193, 129, 206, 129, 195, 129, 202, 129, 201, 129, 221, 129, 223, 129, 197, 129, 213, 132, 151, 167, 141, 222, 131, 204, 221, 221, 200, 195, 201, 133, 206, 246, 201, 246, 221, 134, 156, 240, 240, 132, 150, 223, 200, 217, 216, 223, 195, 141, 221, 134, 159, 167]).decode(),_ns0)
    _dh0 = {85: _ns0['_hf0_0'], 54: _ns0['_hf0_1'], 2: _ns0['_hf0_2'], 1: _ns0['_hf0_3']}
    _tc28 = __import__('time').perf_counter_ns
    _segs = [(0, 5)]
    _tprev = _tc28()
    _ck65 = [22]
    _si24 = 0
    for _seg_vm40, _seg_n92 in _segs:
        _td29 = _tc28() - _tprev
        if _td29 > 5000000000: return None
        _tprev = _tc28()
        if _seg_vm40 == 0:
            _ic0 = 0
            while _pc0 < len(_c0):
              try:
                _ic0 += 1
                _op32 = _ot0[_c0[_pc0] & 0xFF]
                if _op32 in _dh0:
                    _pc0 = _dh0[_op32](_stk0, _loc34, _consts42, _names13, _gl48, _c0, _pc0, _regs0, _shared94, _gregs53)
                    continue
                if _op32 < 80:
                    if _op32 < 25:
                        if _op32 < 17:
                            if _op32 < 6:
                                if _op32 < 4:
                                    if _op32 == 3:
                                        _loc34[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                                    else: _pc0 += 1
                                else:
                                    if _op32 < 5:
                                        if _op32 == 4:
                                            _stk0.append(_gl48[_names13[_c0[_pc0+1]]]); _pc0 += 2
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 5:
                                            _gl48[_names13[_c0[_pc0+1]]] = _stk0.pop(); _pc0 += 2
                                        else: _pc0 += 1
                            else:
                                if _op32 < 8:
                                    if _op32 < 7:
                                        if _op32 == 6:
                                            _stk0.append(_stk0[-1]); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 7:
                                            _stk0.pop(); _pc0 += 1
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 16:
                                        if _op32 == 8:
                                            _stk0[-1], _stk0[-2] = _stk0[-2], _stk0[-1]; _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 16:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 + _b71); _pc0 += 1
                                        else: _pc0 += 1
                        else:
                            if _op32 < 21:
                                if _op32 < 19:
                                    if _op32 < 18:
                                        if _op32 == 17:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 - _b71); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 18:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 * _b71); _pc0 += 1
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 20:
                                        if _op32 == 19:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 % _b71); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 20:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 // _b71); _pc0 += 1
                                        else: _pc0 += 1
                            else:
                                if _op32 < 23:
                                    if _op32 < 22:
                                        if _op32 == 21:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 ** _b71); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 22:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 ^ _b71); _pc0 += 1
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 24:
                                        if _op32 == 23:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 & _b71); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 24:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 | _b71); _pc0 += 1
                                        else: _pc0 += 1
                    else:
                        if _op32 < 51:
                            if _op32 < 34:
                                if _op32 < 32:
                                    if _op32 < 26:
                                        if _op32 == 25:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 << _b71); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 26:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 >> _b71); _pc0 += 1
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 33:
                                        if _op32 == 32:
                                            _stk0.append(-_stk0.pop()); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 33:
                                            _stk0.append(~_stk0.pop()); _pc0 += 1
                                        else: _pc0 += 1
                            else:
                                if _op32 < 49:
                                    if _op32 < 48:
                                        if _op32 == 34:
                                            _stk0.append(not _stk0.pop()); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 48:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 == _b71); _pc0 += 1
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 50:
                                        if _op32 == 49:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 != _b71); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 50:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 < _b71); _pc0 += 1
                                        else: _pc0 += 1
                        else:
                            if _op32 < 56:
                                if _op32 < 53:
                                    if _op32 < 52:
                                        if _op32 == 51:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 > _b71); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 52:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 <= _b71); _pc0 += 1
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 55:
                                        if _op32 == 53:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 >= _b71); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 55:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 is not _b71); _pc0 += 1
                                        else: _pc0 += 1
                            else:
                                if _op32 < 65:
                                    if _op32 < 64:
                                        if _op32 == 56:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 in _b71); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 64:
                                            _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 66:
                                        if _op32 == 65:
                                            _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if _stk0.pop() else _pc0 + 3
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 66:
                                            _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if not _stk0.pop() else _pc0 + 3
                                        else: _pc0 += 1
                else:
                    if _op32 < 128:
                        if _op32 < 89:
                            if _op32 < 84:
                                if _op32 < 82:
                                    if _op32 < 81:
                                        if _op32 == 80:
                                            _tmp45 = _c0[_pc0+1]
                                            if _tmp45: _val28 = _stk0[-_tmp45:]; del _stk0[-_tmp45:]
                                            else: _val28 = []
                                            _stk0.append(_stk0.pop()(*_val28)); _pc0 += 2
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 81:
                                            _stk0.append(getattr(_stk0.pop(), _names13[_c0[_pc0+1]])); _pc0 += 2
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 83:
                                        if _op32 == 82:
                                            _val28 = _stk0.pop(); setattr(_stk0.pop(), _names13[_c0[_pc0+1]], _val28); _pc0 += 2
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 83:
                                            _tmp45 = _c0[_pc0+2]
                                            _val28 = [_stk0.pop() for _ in range(_tmp45)][::-1]
                                            _stk0.append(getattr(_stk0.pop(), _names13[_c0[_pc0+1]])(*_val28)); _pc0 += 3
                                        else: _pc0 += 1
                            else:
                                if _op32 < 87:
                                    if _op32 < 86:
                                        if _op32 == 84:
                                            _tmp45 = _c0[_pc0+1]
                                            if _tmp45: _val28 = _stk0[-_tmp45:]; del _stk0[-_tmp45:]
                                            else: _val28 = []
                                            _stk0.append(_val28); _pc0 += 2
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 86:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87[_b71]); _pc0 += 1
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 88:
                                        if _op32 == 87:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _val28 = _stk0.pop(); _a87[_b71] = _val28; _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 88:
                                            _val28 = list(_stk0.pop())[:_c0[_pc0+1]]; _stk0.extend(reversed(_val28)); _pc0 += 2
                                        else: _pc0 += 1
                        else:
                            if _op32 < 112:
                                if _op32 < 96:
                                    if _op32 < 90:
                                        if _op32 == 89:
                                            _tmp45 = _c0[_pc0+1]; _val28 = {}
                                            for _ in range(_tmp45): _b71 = _stk0.pop(); _a87 = _stk0.pop(); _val28[_a87] = _b71
                                            _stk0.append(_val28); _pc0 += 2
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 90:
                                            _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(slice(_a87, _b71)); _pc0 += 1
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 97:
                                        if _op32 == 96:
                                            _stk0.append(iter(_stk0.pop())); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 97:
                                            _val28 = next(_stk0[-1], None)
                                            if _val28 is None: _stk0.pop(); _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                                            else: _stk0.append(_val28); _pc0 += 3
                                        else: _pc0 += 1
                            else:
                                if _op32 < 121:
                                    if _op32 < 120:
                                        if _op32 == 112:
                                            return _stk0.pop()
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 120:
                                            _eh0.append(_c0[_pc0+1] | (_c0[_pc0+2] << 8)); _pc0 += 3
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 122:
                                        if _op32 == 121:
                                            _eh0.pop(); _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 122:
                                            _tmp45 = _c0[_pc0+1] | (_c0[_pc0+2] << 8); _c0[_tmp45] ^= _c0[_pc0+3]; _pc0 += 4
                                        else: _pc0 += 1
                    else:
                        if _op32 < 145:
                            if _op32 < 132:
                                if _op32 < 130:
                                    if _op32 < 129:
                                        if _op32 == 128:
                                            _regs0[_c0[_pc0+1]] = _loc34[_c0[_pc0+2]]; _pc0 += 3
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 129:
                                            _loc34[_c0[_pc0+2]] = _regs0[_c0[_pc0+1]]; _pc0 += 3
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 131:
                                        if _op32 == 130:
                                            _stk0.append(_regs0[_c0[_pc0+1]]); _pc0 += 2
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 131:
                                            _regs0[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                                        else: _pc0 += 1
                            else:
                                if _op32 < 134:
                                    if _op32 < 133:
                                        if _op32 == 132:
                                            _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+2]]; _pc0 += 3
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 133:
                                            _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] + _regs0[_c0[_pc0+2]]; _pc0 += 3
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 144:
                                        if _op32 == 134:
                                            _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] - _regs0[_c0[_pc0+2]]; _pc0 += 3
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 144:
                                            _shared94[_c0[_pc0+1]].append(_stk0.pop()); _pc0 += 2
                                        else: _pc0 += 1
                        else:
                            if _op32 < 160:
                                if _op32 < 147:
                                    if _op32 < 146:
                                        if _op32 == 145:
                                            _stk0.append(_shared94[_c0[_pc0+1]].pop()); _pc0 += 2
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 146:
                                            _gregs53[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 148:
                                        if _op32 == 147:
                                            _stk0.append(_gregs53[_c0[_pc0+1]]); _pc0 += 2
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 148:
                                            _pc0 += 1; break
                                        else: _pc0 += 1
                            else:
                                if _op32 < 254:
                                    if _op32 < 161:
                                        if _op32 == 160:
                                            _stk0.append(_loc34[_c0[_pc0+1]]); _b71 = _stk0.pop(); _a87 = _stk0.pop(); _stk0.append(_a87 - _b71); _pc0 += 2
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 161:
                                            _loc34[_c0[_pc0+2]] = _consts42[_c0[_pc0+1]]; _pc0 += 3
                                        else: _pc0 += 1
                                else:
                                    if _op32 < 255:
                                        if _op32 == 254:
                                            _pc0 += 1
                                        else: _pc0 += 1
                                    else:
                                        if _op32 == 255:
                                            return _stk0[-1] if _stk0 else None
                                        else: _pc0 += 1
              except Exception as _exc:
                if _eh0: _pc0 = _eh0.pop(); _stk0.append(_exc)
                else: raise
        _hb77 = 0
        _hb77 = (_hb77 + len(_stk0) * 178) & 0xFFFF
        _hb77 = (_hb77 + _pc0 * 147) & 0xFFFF
        if len(_loc34) != 2: return None
        _si24 += 1
    return _stk0[-1] if _stk0 else None
def X8(*_args, **_kwargs):
    return _vm3792(*_args)

def _xn1802(_cs11):
    _r31 = (((((_cs11[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | ((_cs11[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF
    _tmp23 = (_cs11[1] << 17) & 0xFFFFFFFFFFFFFFFF
    _cs11[2] ^= _cs11[0]; _cs11[3] ^= _cs11[1]; _cs11[1] ^= _cs11[2]; _cs11[0] ^= _cs11[3]
    _cs11[2] ^= _tmp23; _cs11[3] = ((_cs11[3] << 45) | (_cs11[3] >> 19)) & 0xFFFFFFFFFFFFFFFF
    return _r31
def _xd1802(_v048, _v150, _k33):
    _delta55 = 0x9E3779B9; _s16 = (_delta55 * 32) & 0xFFFFFFFF
    for _ in range(32):
        _v150 = (_v150 - ((((_v048 << 4) ^ (_v048 >> 5)) + _v048) ^ (_s16 + _k33[(_s16 >> 11) & 3]))) & 0xFFFFFFFF
        _s16 = (_s16 - _delta55) & 0xFFFFFFFF
        _v048 = (_v048 - ((((_v150 << 4) ^ (_v150 >> 5)) + _v150) ^ (_s16 + _k33[_s16 & 3]))) & 0xFFFFFFFF
    return _v048, _v150
def _sh1802(_k33, _code23):
    _sv92 = [int.from_bytes(_k33[:8], 'little') ^ 0x736f6d6570736575, int.from_bytes(_k33[8:], 'little') ^ 0x646f72616e646f6d, int.from_bytes(_k33[:8], 'little') ^ 0x6c7967656e657261, int.from_bytes(_k33[8:], 'little') ^ 0x7465646279746573]
    def _sr():
        _sv92[0] = (_sv92[0] + _sv92[1]) & 0xFFFFFFFFFFFFFFFF; _sv92[1] = ((_sv92[1] << 13) | (_sv92[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ _sv92[0]; _sv92[0] = ((_sv92[0] << 32) | (_sv92[0] >> 32)) & 0xFFFFFFFFFFFFFFFF
        _sv92[2] = (_sv92[2] + _sv92[3]) & 0xFFFFFFFFFFFFFFFF; _sv92[3] = ((_sv92[3] << 16) | (_sv92[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ _sv92[2]
        _sv92[0] = (_sv92[0] + _sv92[3]) & 0xFFFFFFFFFFFFFFFF; _sv92[3] = ((_sv92[3] << 21) | (_sv92[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ _sv92[0]
        _sv92[2] = (_sv92[2] + _sv92[1]) & 0xFFFFFFFFFFFFFFFF; _sv92[1] = ((_sv92[1] << 17) | (_sv92[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ _sv92[2]; _sv92[2] = ((_sv92[2] << 32) | (_sv92[2] >> 32)) & 0xFFFFFFFFFFFFFFFF
    for _bi49 in range(0, len(_code23) - 7, 8):
        _tmp23 = int.from_bytes(_code23[_bi49:_bi49+8], 'little'); _sv92[3] ^= _tmp23; _sr(); _sr(); _sv92[0] ^= _tmp23
    _tmp23 = 0
    for _bi49 in range(len(_code23) & ~7, len(_code23)): _tmp23 |= _code23[_bi49] << (8 * (_bi49 & 7))
    _tmp23 |= (len(_code23) & 0xFF) << 56; _sv92[3] ^= _tmp23; _sr(); _sr(); _sv92[0] ^= _tmp23; _sv92[2] ^= 0xFF; _sr(); _sr(); _sr(); _sr()
    return (_sv92[0] ^ _sv92[1] ^ _sv92[2] ^ _sv92[3]) & 0xFFFFFFFFFFFFFFFF
def _vm1802(*_a96):
    _c3 = bytearray()
    _ek3 = (2147096649, 2413098999, 2140154067, 2724589957)
    _ed3 = [141, 195, 84, 246, 25, 8, 115, 27]
    for _bi49 in range(0, len(_ed3), 8):
        _v048 = (_ed3[_bi49]<<24)|(_ed3[_bi49+1]<<16)|(_ed3[_bi49+2]<<8)|_ed3[_bi49+3]
        _v150 = (_ed3[_bi49+4]<<24)|(_ed3[_bi49+5]<<16)|(_ed3[_bi49+6]<<8)|_ed3[_bi49+7]
        _v048,_v150 = _xd1802(_v048,_v150,_ek3)
        _c3.extend([(_v048>>24)&0xFF,(_v048>>16)&0xFF,(_v048>>8)&0xFF,_v048&0xFF,(_v150>>24)&0xFF,(_v150>>16)&0xFF,(_v150>>8)&0xFF,_v150&0xFF])
    _c3 = _c3[:1]
    if _sh1802(b'\x19{\xb9\xd6\xdci\x16}\xb5QF\xe9\x19j5U', bytes(_c3)) != 10238727437213337066: raise MemoryError()
    _cs3 = [11347883004574293137, 6631865010233429002, 3017939552471609345, 17380507039905880855]
    for _bi49 in range(len(_c3)): _c3[_bi49] ^= _xn1802(_cs3) & 0xFF
    _c4 = bytearray()
    _ek4 = (4031340968, 1645502492, 3400724448, 1682323721)
    _ed4 = [53, 251, 128, 143, 250, 240, 95, 227]
    for _bi49 in range(0, len(_ed4), 8):
        _v048 = (_ed4[_bi49]<<24)|(_ed4[_bi49+1]<<16)|(_ed4[_bi49+2]<<8)|_ed4[_bi49+3]
        _v150 = (_ed4[_bi49+4]<<24)|(_ed4[_bi49+5]<<16)|(_ed4[_bi49+6]<<8)|_ed4[_bi49+7]
        _v048,_v150 = _xd1802(_v048,_v150,_ek4)
        _c4.extend([(_v048>>24)&0xFF,(_v048>>16)&0xFF,(_v048>>8)&0xFF,_v048&0xFF,(_v150>>24)&0xFF,(_v150>>16)&0xFF,(_v150>>8)&0xFF,_v150&0xFF])
    _c0 = bytearray()
    _ek0 = (3833333329, 1978397774, 2558637714, 3192214689)
    _ed0 = [199, 140, 76, 40, 111, 22, 144, 18, 2, 134, 9, 211, 73, 216, 9, 64, 37, 32, 238, 100, 66, 7, 67, 205, 30, 234, 189, 128, 76, 128, 170, 49, 184, 48, 93, 42, 16, 82, 189, 189, 168, 80, 51, 98, 76, 230, 203, 165, 186, 185, 235, 218, 246, 167, 128, 178, 3, 59, 235, 200, 244, 128, 178, 153, 237, 54, 189, 42, 30, 159, 236, 76]
    for _bi49 in range(0, len(_ed0), 8):
        _v048 = (_ed0[_bi49]<<24)|(_ed0[_bi49+1]<<16)|(_ed0[_bi49+2]<<8)|_ed0[_bi49+3]
        _v150 = (_ed0[_bi49+4]<<24)|(_ed0[_bi49+5]<<16)|(_ed0[_bi49+6]<<8)|_ed0[_bi49+7]
        _v048,_v150 = _xd1802(_v048,_v150,_ek0)
        _c0.extend([(_v048>>24)&0xFF,(_v048>>16)&0xFF,(_v048>>8)&0xFF,_v048&0xFF,(_v150>>24)&0xFF,(_v150>>16)&0xFF,(_v150>>8)&0xFF,_v150&0xFF])
    _c0 = _c0[:68]
    if _sh1802(b'\x19{\xb9\xd6\xdci\x16}\xb5QF\xe9\x19j5U', bytes(_c0)) != 17162223005945744965: raise MemoryError()
    _cs0 = [17290175861907928818, 17828554581934683390, 4392928267905883827, 5606813200709498040]
    for _bi49 in range(len(_c0)): _c0[_bi49] ^= _xn1802(_cs0) & 0xFF
    _c1 = bytearray()
    _ek1 = (3982069879, 3345925362, 3753575134, 2874896464)
    _ed1 = [171, 224, 194, 16, 108, 136, 79, 140]
    for _bi49 in range(0, len(_ed1), 8):
        _v048 = (_ed1[_bi49]<<24)|(_ed1[_bi49+1]<<16)|(_ed1[_bi49+2]<<8)|_ed1[_bi49+3]
        _v150 = (_ed1[_bi49+4]<<24)|(_ed1[_bi49+5]<<16)|(_ed1[_bi49+6]<<8)|_ed1[_bi49+7]
        _v048,_v150 = _xd1802(_v048,_v150,_ek1)
        _c1.extend([(_v048>>24)&0xFF,(_v048>>16)&0xFF,(_v048>>8)&0xFF,_v048&0xFF,(_v150>>24)&0xFF,(_v150>>16)&0xFF,(_v150>>8)&0xFF,_v150&0xFF])
    _c1 = _c1[:1]
    if _sh1802(b'\x19{\xb9\xd6\xdci\x16}\xb5QF\xe9\x19j5U', bytes(_c1)) != 16639300459073922022: raise MemoryError()
    _cs1 = [10001669838911747831, 783454568619529057, 2701197842535496963, 17081057527400797643]
    for _bi49 in range(len(_c1)): _c1[_bi49] ^= _xn1802(_cs1) & 0xFF
    _c2 = bytearray()
    _ek2 = (1808957137, 1680850746, 3015641603, 2302809424)
    _ed2 = [243, 215, 27, 186, 52, 56, 34, 117]
    for _bi49 in range(0, len(_ed2), 8):
        _v048 = (_ed2[_bi49]<<24)|(_ed2[_bi49+1]<<16)|(_ed2[_bi49+2]<<8)|_ed2[_bi49+3]
        _v150 = (_ed2[_bi49+4]<<24)|(_ed2[_bi49+5]<<16)|(_ed2[_bi49+6]<<8)|_ed2[_bi49+7]
        _v048,_v150 = _xd1802(_v048,_v150,_ek2)
        _c2.extend([(_v048>>24)&0xFF,(_v048>>16)&0xFF,(_v048>>8)&0xFF,_v048&0xFF,(_v150>>24)&0xFF,(_v150>>16)&0xFF,(_v150>>8)&0xFF,_v150&0xFF])
    _c2 = _c2[:4]
    if _sh1802(b'\x19{\xb9\xd6\xdci\x16}\xb5QF\xe9\x19j5U', bytes(_c2)) != 17371064289357659275: raise MemoryError()
    _cs2 = [10368885273466676847, 15907754317002646755, 4818658546096253251, 10241130418909652214]
    for _bi49 in range(len(_c2)): _c2[_bi49] ^= _xn1802(_cs2) & 0xFF
    _shared70 = [[] for _ in range(3)]
    _gregs41 = [None] * 4
    _loc36 = list(_a96[:1]) + [None] * 2
    _consts14 = [0, True, 1405205, 1405204, 100]
    _names39 = []
    _gl31 = globals()
    _gl31.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))
    _ot0 = [166, 8, 68, 245, 222, 189, 44, 243, 47, 204, 158, 65, 164, 12, 76, 30, 219, 202, 90, 228, 250, 209, 43, 235, 230, 48, 133, 60, 94, 253, 195, 200, 100, 182, 237, 33, 35, 186, 207, 19, 238, 107, 221, 79, 194, 162, 161, 177, 229, 72, 169, 41, 191, 45, 63, 112, 78, 175, 25, 4, 131, 50, 102, 61, 255, 140, 91, 150, 55, 56, 223, 173, 240, 109, 59, 168, 170, 239, 156, 247, 120, 23, 217, 163, 193, 114, 234, 27, 11, 113, 146, 124, 20, 188, 220, 101, 134, 7, 105, 251, 241, 93, 213, 137, 201, 138, 242, 199, 215, 174, 28, 185, 92, 142, 214, 49, 67, 54, 165, 171, 46, 74, 197, 132, 77, 190, 3, 152, 249, 136, 184, 108, 159, 126, 216, 119, 155, 143, 203, 187, 21, 1, 178, 73, 128, 17, 26, 32, 208, 236, 135, 69, 110, 98, 115, 18, 176, 99, 225, 51, 192, 31, 151, 15, 82, 38, 84, 13, 160, 179, 87, 83, 231, 70, 227, 144, 218, 121, 157, 97, 2, 147, 88, 9, 205, 10, 254, 103, 212, 40, 206, 145, 224, 16, 85, 130, 52, 86, 42, 248, 153, 71, 81, 95, 139, 64, 36, 75, 127, 37, 125, 96, 198, 154, 80, 66, 210, 58, 111, 181, 149, 106, 104, 180, 116, 244, 22, 196, 53, 129, 5, 211, 39, 172, 226, 62, 233, 123, 0, 117, 24, 57, 34, 232, 14, 246, 6, 148, 29, 183, 167, 89, 141, 122, 252, 118]
    _stk0 = []
    _pc0 = 0
    _regs0 = [None] * 8
    _eh0 = []
    _ns0 = {}
    exec(bytes(b^165 for b in [193, 192, 195, 133, 250, 205, 195, 149, 250, 149, 141, 214, 137, 201, 137, 198, 137, 203, 137, 194, 137, 193, 137, 213, 137, 215, 137, 205, 137, 221, 140, 159, 175, 133, 199, 152, 214, 139, 213, 202, 213, 141, 140, 158, 196, 152, 214, 139, 213, 202, 213, 141, 140, 158, 214, 139, 196, 213, 213, 192, 203, 193, 141, 196, 142, 199, 140, 158, 215, 192, 209, 208, 215, 203, 133, 213, 142, 148, 175, 193, 192, 195, 133, 250, 205, 195, 149, 250, 148, 141, 214, 137, 201, 137, 198, 137, 203, 137, 194, 137, 193, 137, 213, 137, 215, 137, 205, 137, 221, 140, 159, 175, 133, 199, 152, 214, 139, 213, 202, 213, 141, 140, 158, 196, 152, 214, 139, 213, 202, 213, 141, 140, 158, 214, 139, 196, 213, 213, 192, 203, 193, 141, 196, 155, 152, 199, 140, 158, 215, 192, 209, 208, 215, 203, 133, 213, 142, 148, 175, 193, 192, 195, 133, 250, 205, 195, 149, 250, 151, 141, 214, 137, 201, 137, 198, 137, 203, 137, 194, 137, 193, 137, 213, 137, 215, 137, 205, 137, 221, 140, 159, 175, 133, 214, 139, 196, 213, 213, 192, 203, 193, 141, 136, 214, 139, 213, 202, 213, 141, 140, 140, 158, 215, 192, 209, 208, 215, 203, 133, 213, 142, 148, 175, 193, 192, 195, 133, 250, 205, 195, 149, 250, 150, 141, 214, 137, 201, 137, 198, 137, 203, 137, 194, 137, 193, 137, 213, 137, 215, 137, 205, 137, 221, 140, 159, 175, 133, 215, 254, 193, 254, 213, 142, 148, 248, 248, 152, 201, 254, 193, 254, 213, 142, 151, 248, 248, 158, 215, 192, 209, 208, 215, 203, 133, 213, 142, 150, 175]).decode(),_ns0)
    _dh0 = {16: _ns0['_hf0_0'], 53: _ns0['_hf0_1'], 32: _ns0['_hf0_2'], 128: _ns0['_hf0_3']}
    _ot1 = [17, 4, 241, 89, 165, 65, 181, 134, 169, 108, 12, 151, 152, 172, 250, 111, 246, 81, 162, 60, 9, 36, 23, 125, 49, 157, 58, 179, 88, 247, 7, 137, 251, 144, 59, 142, 253, 229, 143, 227, 198, 149, 109, 26, 204, 16, 122, 121, 42, 224, 34, 124, 133, 240, 166, 120, 183, 84, 104, 99, 235, 53, 0, 47, 115, 191, 163, 156, 201, 127, 118, 1, 192, 207, 112, 24, 234, 76, 114, 140, 56, 103, 79, 73, 52, 197, 46, 203, 255, 211, 116, 158, 128, 83, 228, 164, 78, 170, 85, 236, 242, 230, 150, 8, 171, 174, 206, 196, 245, 213, 199, 102, 19, 101, 200, 105, 189, 38, 212, 185, 194, 155, 10, 202, 222, 208, 39, 119, 195, 244, 146, 87, 186, 154, 64, 45, 70, 44, 91, 131, 29, 61, 27, 90, 239, 82, 55, 123, 231, 35, 18, 160, 20, 145, 220, 117, 148, 2, 37, 130, 147, 25, 54, 32, 57, 28, 215, 190, 96, 254, 135, 68, 153, 233, 11, 31, 225, 223, 51, 129, 100, 167, 97, 136, 184, 177, 178, 50, 232, 5, 33, 69, 40, 126, 30, 188, 77, 113, 176, 98, 94, 92, 139, 86, 93, 14, 74, 210, 21, 216, 249, 218, 62, 243, 252, 237, 248, 159, 95, 6, 63, 132, 217, 107, 80, 66, 180, 15, 173, 106, 175, 214, 72, 67, 41, 182, 13, 141, 221, 168, 138, 161, 238, 205, 48, 226, 3, 75, 219, 43, 209, 110, 22, 71, 187, 193]
    _stk1 = []
    _pc1 = 0
    _regs1 = [None] * 8
    _eh1 = []
    _dh1 = {}
    _ot2 = [9, 136, 140, 13, 203, 169, 57, 216, 144, 37, 107, 161, 215, 225, 193, 82, 5, 209, 238, 3, 62, 66, 188, 159, 131, 207, 231, 135, 204, 71, 220, 101, 166, 110, 138, 58, 8, 183, 16, 246, 119, 174, 184, 232, 240, 177, 87, 11, 167, 219, 59, 55, 63, 80, 44, 196, 56, 195, 124, 86, 27, 185, 100, 104, 175, 202, 243, 105, 106, 69, 84, 49, 147, 152, 39, 190, 189, 68, 73, 142, 205, 14, 97, 129, 91, 128, 146, 90, 12, 81, 125, 151, 40, 137, 178, 158, 143, 118, 170, 51, 198, 92, 164, 154, 64, 35, 99, 88, 122, 236, 227, 45, 28, 53, 20, 94, 19, 234, 210, 60, 123, 31, 115, 96, 253, 46, 217, 187, 112, 1, 24, 70, 77, 79, 109, 250, 155, 222, 127, 162, 108, 75, 223, 121, 165, 179, 38, 213, 76, 67, 103, 212, 15, 25, 249, 182, 85, 52, 116, 228, 181, 48, 130, 248, 149, 226, 180, 36, 98, 201, 145, 139, 251, 211, 95, 6, 141, 148, 157, 126, 197, 191, 93, 168, 0, 192, 235, 30, 10, 163, 50, 186, 23, 47, 2, 41, 111, 83, 72, 230, 21, 247, 221, 206, 173, 42, 241, 224, 176, 133, 244, 134, 18, 114, 32, 22, 132, 245, 120, 26, 29, 65, 54, 229, 239, 78, 61, 156, 43, 233, 34, 33, 172, 17, 214, 218, 102, 153, 255, 242, 160, 194, 113, 7, 254, 200, 199, 4, 150, 252, 171, 208, 237, 117, 89, 74]
    _stk2 = []
    _pc2 = 0
    _regs2 = [None] * 8
    _eh2 = []
    _ns2 = {}
    exec(bytes(b^84 for b in [48, 49, 50, 116, 11, 60, 50, 102, 11, 100, 124, 39, 120, 56, 120, 55, 120, 58, 120, 51, 120, 48, 120, 36, 120, 38, 120, 60, 120, 44, 125, 110, 94, 116, 54, 105, 39, 122, 36, 59, 36, 124, 125, 111, 53, 105, 39, 122, 36, 59, 36, 124, 125, 111, 39, 122, 53, 36, 36, 49, 58, 48, 124, 53, 116, 61, 39, 116, 58, 59, 32, 116, 54, 125, 111, 38, 49, 32, 33, 38, 58, 116, 36, 127, 101, 94, 48, 49, 50, 116, 11, 60, 50, 102, 11, 101, 124, 39, 120, 56, 120, 55, 120, 58, 120, 51, 120, 48, 120, 36, 120, 38, 120, 60, 120, 44, 125, 110, 94, 116, 56, 15, 48, 15, 36, 127, 102, 9, 9, 105, 55, 15, 48, 15, 36, 127, 101, 9, 9, 111, 38, 49, 32, 33, 38, 58, 116, 36, 127, 103, 94, 48, 49, 50, 116, 11, 60, 50, 102, 11, 102, 124, 39, 120, 56, 120, 55, 120, 58, 120, 51, 120, 48, 120, 36, 120, 38, 120, 60, 120, 44, 125, 110, 94, 116, 38, 15, 48, 15, 36, 127, 101, 9, 9, 105, 38, 15, 48, 15, 36, 127, 102, 9, 9, 111, 38, 49, 32, 33, 38, 58, 116, 36, 127, 103, 94]).decode(),_ns2)
    _dh2 = {55: _ns2['_hf2_0'], 160: _ns2['_hf2_1'], 132: _ns2['_hf2_2']}
    _ot3 = [96, 139, 128, 6, 82, 28, 169, 121, 149, 48, 208, 9, 248, 10, 24, 74, 214, 36, 76, 102, 185, 246, 137, 213, 122, 38, 184, 112, 193, 217, 164, 200, 138, 106, 110, 30, 130, 142, 252, 171, 15, 152, 41, 58, 157, 244, 67, 12, 162, 65, 165, 71, 53, 27, 91, 207, 77, 202, 124, 113, 0, 16, 25, 35, 87, 204, 229, 132, 78, 225, 109, 61, 34, 37, 143, 13, 100, 56, 107, 148, 222, 160, 154, 187, 66, 62, 153, 129, 141, 188, 81, 5, 80, 51, 101, 175, 117, 245, 93, 151, 191, 186, 140, 44, 7, 215, 46, 21, 237, 251, 230, 4, 220, 247, 11, 72, 119, 40, 111, 136, 20, 32, 8, 242, 155, 226, 201, 249, 224, 105, 174, 57, 231, 223, 17, 240, 55, 144, 236, 168, 195, 166, 196, 19, 3, 183, 49, 189, 73, 167, 150, 241, 156, 103, 243, 146, 75, 182, 108, 126, 216, 1, 199, 94, 90, 50, 88, 92, 145, 147, 250, 205, 233, 163, 83, 79, 123, 63, 70, 115, 45, 95, 254, 22, 135, 173, 232, 178, 219, 116, 68, 198, 212, 85, 89, 180, 64, 197, 60, 54, 177, 14, 120, 127, 203, 210, 235, 43, 26, 221, 194, 181, 42, 239, 192, 161, 18, 114, 133, 99, 253, 159, 238, 176, 84, 52, 97, 234, 2, 190, 59, 47, 179, 31, 134, 170, 206, 39, 33, 98, 172, 118, 228, 211, 227, 131, 158, 209, 69, 104, 125, 255, 86, 218, 23, 29]
    _stk3 = []
    _pc3 = 0
    _regs3 = [None] * 8
    _eh3 = []
    _dh3 = {}
    _tc83 = __import__('time').perf_counter_ns
    _segs = [(0, 1), (2, 1), (0, 9)]
    _tprev = _tc83()
    _ck14 = [27, 2, 27]
    _si83 = 0
    for _seg_vm37, _seg_n56 in _segs:
        _td36 = _tc83() - _tprev
        if _td36 > 5000000000: return None
        _tprev = _tc83()
        if _seg_vm37 == 0:
            _ic0 = 0
            while _pc0 < len(_c0):
              try:
                _ic0 += 1
                _op52 = _ot0[_c0[_pc0] & 0xFF]
                if _op52 in _dh0:
                    _pc0 = _dh0[_op52](_stk0, _loc36, _consts14, _names39, _gl31, _c0, _pc0, _regs0, _shared70, _gregs41)
                    continue
                _ha098 = [255, 0, 1, 2, 3, 4, 5, 6, 7, 255, 255, 255, 255, 255, 255, 255, 255, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 255, 255, 255, 255, 255, 255, 18, 19, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 20, 21, 22, 23, 24, 255, 25, 26, 27, 255, 255, 255, 255, 255, 255, 255, 28, 29, 30, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 255, 255, 255, 255, 255, 42, 43, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 44, 255, 255, 255, 255, 255, 255, 255, 45, 46, 47, 255, 255, 255, 255, 255, 255, 48, 49, 50, 51, 52, 53, 255, 255, 255, 255, 255, 255, 255, 255, 255, 54, 55, 56, 57, 58, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 59, 60, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 61, 62]
                _ai065 = _ha098[_op52]
                if _ai065 == 0:
                    _stk0.append(_consts14[_c0[_pc0+1]]); _pc0 += 2
                elif _ai065 == 1:
                    _stk0.append(_loc36[_c0[_pc0+1]]); _pc0 += 2
                elif _ai065 == 2:
                    _loc36[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _ai065 == 3:
                    _stk0.append(_gl31[_names39[_c0[_pc0+1]]]); _pc0 += 2
                elif _ai065 == 4:
                    _gl31[_names39[_c0[_pc0+1]]] = _stk0.pop(); _pc0 += 2
                elif _ai065 == 5:
                    _stk0.append(_stk0[-1]); _pc0 += 1
                elif _ai065 == 6:
                    _stk0.pop(); _pc0 += 1
                elif _ai065 == 7:
                    _stk0[-1], _stk0[-2] = _stk0[-2], _stk0[-1]; _pc0 += 1
                elif _ai065 == 8:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 - _b41); _pc0 += 1
                elif _ai065 == 9:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 * _b41); _pc0 += 1
                elif _ai065 == 10:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 % _b41); _pc0 += 1
                elif _ai065 == 11:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 // _b41); _pc0 += 1
                elif _ai065 == 12:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 ** _b41); _pc0 += 1
                elif _ai065 == 13:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 ^ _b41); _pc0 += 1
                elif _ai065 == 14:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 & _b41); _pc0 += 1
                elif _ai065 == 15:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 | _b41); _pc0 += 1
                elif _ai065 == 16:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 << _b41); _pc0 += 1
                elif _ai065 == 17:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 >> _b41); _pc0 += 1
                elif _ai065 == 18:
                    _stk0.append(~_stk0.pop()); _pc0 += 1
                elif _ai065 == 19:
                    _stk0.append(not _stk0.pop()); _pc0 += 1
                elif _ai065 == 20:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 == _b41); _pc0 += 1
                elif _ai065 == 21:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 != _b41); _pc0 += 1
                elif _ai065 == 22:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 < _b41); _pc0 += 1
                elif _ai065 == 23:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 > _b41); _pc0 += 1
                elif _ai065 == 24:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 <= _b41); _pc0 += 1
                elif _ai065 == 25:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 is _b41); _pc0 += 1
                elif _ai065 == 26:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 is not _b41); _pc0 += 1
                elif _ai065 == 27:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 in _b41); _pc0 += 1
                elif _ai065 == 28:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                elif _ai065 == 29:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if _stk0.pop() else _pc0 + 3
                elif _ai065 == 30:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if not _stk0.pop() else _pc0 + 3
                elif _ai065 == 31:
                    _tmp23 = _c0[_pc0+1]
                    if _tmp23: _val55 = _stk0[-_tmp23:]; del _stk0[-_tmp23:]
                    else: _val55 = []
                    _stk0.append(_stk0.pop()(*_val55)); _pc0 += 2
                elif _ai065 == 32:
                    _stk0.append(getattr(_stk0.pop(), _names39[_c0[_pc0+1]])); _pc0 += 2
                elif _ai065 == 33:
                    _val55 = _stk0.pop(); setattr(_stk0.pop(), _names39[_c0[_pc0+1]], _val55); _pc0 += 2
                elif _ai065 == 34:
                    _tmp23 = _c0[_pc0+2]
                    _val55 = [_stk0.pop() for _ in range(_tmp23)][::-1]
                    _stk0.append(getattr(_stk0.pop(), _names39[_c0[_pc0+1]])(*_val55)); _pc0 += 3
                elif _ai065 == 35:
                    _tmp23 = _c0[_pc0+1]
                    if _tmp23: _val55 = _stk0[-_tmp23:]; del _stk0[-_tmp23:]
                    else: _val55 = []
                    _stk0.append(_val55); _pc0 += 2
                elif _ai065 == 36:
                    _tmp23 = _c0[_pc0+1]
                    if _tmp23: _val55 = tuple(_stk0[-_tmp23:]); del _stk0[-_tmp23:]
                    else: _val55 = ()
                    _stk0.append(_val55); _pc0 += 2
                elif _ai065 == 37:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96[_b41]); _pc0 += 1
                elif _ai065 == 38:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _val55 = _stk0.pop(); _a96[_b41] = _val55; _pc0 += 1
                elif _ai065 == 39:
                    _val55 = list(_stk0.pop())[:_c0[_pc0+1]]; _stk0.extend(reversed(_val55)); _pc0 += 2
                elif _ai065 == 40:
                    _tmp23 = _c0[_pc0+1]; _val55 = {}
                    for _ in range(_tmp23): _b41 = _stk0.pop(); _a96 = _stk0.pop(); _val55[_a96] = _b41
                    _stk0.append(_val55); _pc0 += 2
                elif _ai065 == 41:
                    _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(slice(_a96, _b41)); _pc0 += 1
                elif _ai065 == 42:
                    _stk0.append(iter(_stk0.pop())); _pc0 += 1
                elif _ai065 == 43:
                    _val55 = next(_stk0[-1], None)
                    if _val55 is None: _stk0.pop(); _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                    else: _stk0.append(_val55); _pc0 += 3
                elif _ai065 == 44:
                    return _stk0.pop()
                elif _ai065 == 45:
                    _eh0.append(_c0[_pc0+1] | (_c0[_pc0+2] << 8)); _pc0 += 3
                elif _ai065 == 46:
                    _eh0.pop(); _pc0 += 1
                elif _ai065 == 47:
                    _tmp23 = _c0[_pc0+1] | (_c0[_pc0+2] << 8); _c0[_tmp23] ^= _c0[_pc0+3]; _pc0 += 4
                elif _ai065 == 48:
                    _loc36[_c0[_pc0+2]] = _regs0[_c0[_pc0+1]]; _pc0 += 3
                elif _ai065 == 49:
                    _stk0.append(_regs0[_c0[_pc0+1]]); _pc0 += 2
                elif _ai065 == 50:
                    _regs0[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _ai065 == 51:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _ai065 == 52:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] + _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _ai065 == 53:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] - _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _ai065 == 54:
                    _shared70[_c0[_pc0+1]].append(_stk0.pop()); _pc0 += 2
                elif _ai065 == 55:
                    _stk0.append(_shared70[_c0[_pc0+1]].pop()); _pc0 += 2
                elif _ai065 == 56:
                    _gregs41[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _ai065 == 57:
                    _stk0.append(_gregs41[_c0[_pc0+1]]); _pc0 += 2
                elif _ai065 == 58:
                    _pc0 += 1; break
                elif _ai065 == 59:
                    _loc36[_c0[_pc0+2]] = _consts14[_c0[_pc0+1]]; _pc0 += 3
                elif _ai065 == 60:
                    _stk0.append(_loc36[_c0[_pc0+1]]); _b41 = _stk0.pop(); _a96 = _stk0.pop(); _stk0.append(_a96 + _b41); _pc0 += 2
                elif _ai065 == 61:
                    _pc0 += 1
                elif _ai065 == 62:
                    return _stk0[-1] if _stk0 else None
                else: _pc0 += 1
              except Exception as _exc:
                if _eh0: _pc0 = _eh0.pop(); _stk0.append(_exc)
                else: raise
        elif _seg_vm37 == 1:
            _ic1 = 0
            while _pc1 < len(_c1):
              try:
                _ic1 += 1
                _op52 = _ot1[_c1[_pc1] & 0xFF]
                _ha175 = [255, 0, 1, 2, 3, 4, 5, 6, 7, 255, 255, 255, 255, 255, 255, 255, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 255, 255, 255, 255, 255, 19, 20, 21, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 22, 23, 24, 25, 26, 27, 28, 29, 30, 255, 255, 255, 255, 255, 255, 255, 31, 32, 33, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 255, 255, 255, 255, 255, 45, 46, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 47, 255, 255, 255, 255, 255, 255, 255, 48, 49, 50, 255, 255, 255, 255, 255, 51, 52, 53, 54, 55, 56, 57, 255, 255, 255, 255, 255, 255, 255, 255, 255, 58, 59, 60, 61, 62, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 64, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 65, 66]
                _ai160 = _ha175[_op52]
                if _ai160 == 0:
                    _stk1.append(_consts14[_c1[_pc1+1]]); _pc1 += 2
                elif _ai160 == 1:
                    _stk1.append(_loc36[_c1[_pc1+1]]); _pc1 += 2
                elif _ai160 == 2:
                    _loc36[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _ai160 == 3:
                    _stk1.append(_gl31[_names39[_c1[_pc1+1]]]); _pc1 += 2
                elif _ai160 == 4:
                    _gl31[_names39[_c1[_pc1+1]]] = _stk1.pop(); _pc1 += 2
                elif _ai160 == 5:
                    _stk1.append(_stk1[-1]); _pc1 += 1
                elif _ai160 == 6:
                    _stk1.pop(); _pc1 += 1
                elif _ai160 == 7:
                    _stk1[-1], _stk1[-2] = _stk1[-2], _stk1[-1]; _pc1 += 1
                elif _ai160 == 8:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 + _b41); _pc1 += 1
                elif _ai160 == 9:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 - _b41); _pc1 += 1
                elif _ai160 == 10:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 * _b41); _pc1 += 1
                elif _ai160 == 11:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 % _b41); _pc1 += 1
                elif _ai160 == 12:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 // _b41); _pc1 += 1
                elif _ai160 == 13:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 ** _b41); _pc1 += 1
                elif _ai160 == 14:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 ^ _b41); _pc1 += 1
                elif _ai160 == 15:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 & _b41); _pc1 += 1
                elif _ai160 == 16:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 | _b41); _pc1 += 1
                elif _ai160 == 17:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 << _b41); _pc1 += 1
                elif _ai160 == 18:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 >> _b41); _pc1 += 1
                elif _ai160 == 19:
                    _stk1.append(-_stk1.pop()); _pc1 += 1
                elif _ai160 == 20:
                    _stk1.append(~_stk1.pop()); _pc1 += 1
                elif _ai160 == 21:
                    _stk1.append(not _stk1.pop()); _pc1 += 1
                elif _ai160 == 22:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 == _b41); _pc1 += 1
                elif _ai160 == 23:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 != _b41); _pc1 += 1
                elif _ai160 == 24:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 < _b41); _pc1 += 1
                elif _ai160 == 25:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 > _b41); _pc1 += 1
                elif _ai160 == 26:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 <= _b41); _pc1 += 1
                elif _ai160 == 27:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 >= _b41); _pc1 += 1
                elif _ai160 == 28:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 is _b41); _pc1 += 1
                elif _ai160 == 29:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 is not _b41); _pc1 += 1
                elif _ai160 == 30:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 in _b41); _pc1 += 1
                elif _ai160 == 31:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                elif _ai160 == 32:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if _stk1.pop() else _pc1 + 3
                elif _ai160 == 33:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if not _stk1.pop() else _pc1 + 3
                elif _ai160 == 34:
                    _tmp23 = _c1[_pc1+1]
                    if _tmp23: _val55 = _stk1[-_tmp23:]; del _stk1[-_tmp23:]
                    else: _val55 = []
                    _stk1.append(_stk1.pop()(*_val55)); _pc1 += 2
                elif _ai160 == 35:
                    _stk1.append(getattr(_stk1.pop(), _names39[_c1[_pc1+1]])); _pc1 += 2
                elif _ai160 == 36:
                    _val55 = _stk1.pop(); setattr(_stk1.pop(), _names39[_c1[_pc1+1]], _val55); _pc1 += 2
                elif _ai160 == 37:
                    _tmp23 = _c1[_pc1+2]
                    _val55 = [_stk1.pop() for _ in range(_tmp23)][::-1]
                    _stk1.append(getattr(_stk1.pop(), _names39[_c1[_pc1+1]])(*_val55)); _pc1 += 3
                elif _ai160 == 38:
                    _tmp23 = _c1[_pc1+1]
                    if _tmp23: _val55 = _stk1[-_tmp23:]; del _stk1[-_tmp23:]
                    else: _val55 = []
                    _stk1.append(_val55); _pc1 += 2
                elif _ai160 == 39:
                    _tmp23 = _c1[_pc1+1]
                    if _tmp23: _val55 = tuple(_stk1[-_tmp23:]); del _stk1[-_tmp23:]
                    else: _val55 = ()
                    _stk1.append(_val55); _pc1 += 2
                elif _ai160 == 40:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96[_b41]); _pc1 += 1
                elif _ai160 == 41:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _val55 = _stk1.pop(); _a96[_b41] = _val55; _pc1 += 1
                elif _ai160 == 42:
                    _val55 = list(_stk1.pop())[:_c1[_pc1+1]]; _stk1.extend(reversed(_val55)); _pc1 += 2
                elif _ai160 == 43:
                    _tmp23 = _c1[_pc1+1]; _val55 = {}
                    for _ in range(_tmp23): _b41 = _stk1.pop(); _a96 = _stk1.pop(); _val55[_a96] = _b41
                    _stk1.append(_val55); _pc1 += 2
                elif _ai160 == 44:
                    _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(slice(_a96, _b41)); _pc1 += 1
                elif _ai160 == 45:
                    _stk1.append(iter(_stk1.pop())); _pc1 += 1
                elif _ai160 == 46:
                    _val55 = next(_stk1[-1], None)
                    if _val55 is None: _stk1.pop(); _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                    else: _stk1.append(_val55); _pc1 += 3
                elif _ai160 == 47:
                    return _stk1.pop()
                elif _ai160 == 48:
                    _eh1.append(_c1[_pc1+1] | (_c1[_pc1+2] << 8)); _pc1 += 3
                elif _ai160 == 49:
                    _eh1.pop(); _pc1 += 1
                elif _ai160 == 50:
                    _tmp23 = _c1[_pc1+1] | (_c1[_pc1+2] << 8); _c1[_tmp23] ^= _c1[_pc1+3]; _pc1 += 4
                elif _ai160 == 51:
                    _regs1[_c1[_pc1+1]] = _loc36[_c1[_pc1+2]]; _pc1 += 3
                elif _ai160 == 52:
                    _loc36[_c1[_pc1+2]] = _regs1[_c1[_pc1+1]]; _pc1 += 3
                elif _ai160 == 53:
                    _stk1.append(_regs1[_c1[_pc1+1]]); _pc1 += 2
                elif _ai160 == 54:
                    _regs1[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _ai160 == 55:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _ai160 == 56:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] + _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _ai160 == 57:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] - _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _ai160 == 58:
                    _shared70[_c1[_pc1+1]].append(_stk1.pop()); _pc1 += 2
                elif _ai160 == 59:
                    _stk1.append(_shared70[_c1[_pc1+1]].pop()); _pc1 += 2
                elif _ai160 == 60:
                    _gregs41[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _ai160 == 61:
                    _stk1.append(_gregs41[_c1[_pc1+1]]); _pc1 += 2
                elif _ai160 == 62:
                    _pc1 += 1; break
                elif _ai160 == 63:
                    _loc36[_c1[_pc1+2]] = _consts14[_c1[_pc1+1]]; _pc1 += 3
                elif _ai160 == 64:
                    _stk1.append(_loc36[_c1[_pc1+1]]); _b41 = _stk1.pop(); _a96 = _stk1.pop(); _stk1.append(_a96 + _b41); _pc1 += 2
                elif _ai160 == 65:
                    _pc1 += 1
                elif _ai160 == 66:
                    return _stk1[-1] if _stk1 else None
                else: _pc1 += 1
              except Exception as _exc:
                if _eh1: _pc1 = _eh1.pop(); _stk1.append(_exc)
                else: raise
        elif _seg_vm37 == 2:
            _ic2 = 0
            while _pc2 < len(_c2):
              try:
                _ic2 += 1
                _op52 = _ot2[_c2[_pc2] & 0xFF]
                if _op52 in _dh2:
                    _pc2 = _dh2[_op52](_stk2, _loc36, _consts14, _names39, _gl31, _c2, _pc2, _regs2, _shared70, _gregs41)
                    continue
                _dt290 = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 16: 8, 17: 9, 18: 10, 19: 11, 20: 12, 21: 13, 22: 14, 23: 15, 24: 16, 25: 17, 26: 18, 32: 19, 33: 20, 34: 21, 48: 22, 49: 23, 50: 24, 51: 25, 52: 26, 53: 27, 54: 28, 56: 29, 64: 30, 65: 31, 66: 32, 80: 33, 81: 34, 82: 35, 83: 36, 84: 37, 85: 38, 86: 39, 87: 40, 88: 41, 89: 42, 90: 43, 96: 44, 97: 45, 112: 46, 120: 47, 121: 48, 122: 49, 128: 50, 129: 51, 130: 52, 131: 53, 133: 54, 134: 55, 144: 56, 145: 57, 146: 58, 147: 59, 148: 60, 161: 61, 254: 62, 255: 63}
                _hi275 = _dt290.get(_op52, -1)
                if _hi275 == 0:
                    _stk2.append(_consts14[_c2[_pc2+1]]); _pc2 += 2
                elif _hi275 == 1:
                    _stk2.append(_loc36[_c2[_pc2+1]]); _pc2 += 2
                elif _hi275 == 2:
                    _loc36[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _hi275 == 3:
                    _stk2.append(_gl31[_names39[_c2[_pc2+1]]]); _pc2 += 2
                elif _hi275 == 4:
                    _gl31[_names39[_c2[_pc2+1]]] = _stk2.pop(); _pc2 += 2
                elif _hi275 == 5:
                    _stk2.append(_stk2[-1]); _pc2 += 1
                elif _hi275 == 6:
                    _stk2.pop(); _pc2 += 1
                elif _hi275 == 7:
                    _stk2[-1], _stk2[-2] = _stk2[-2], _stk2[-1]; _pc2 += 1
                elif _hi275 == 8:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 + _b41); _pc2 += 1
                elif _hi275 == 9:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 - _b41); _pc2 += 1
                elif _hi275 == 10:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 * _b41); _pc2 += 1
                elif _hi275 == 11:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 % _b41); _pc2 += 1
                elif _hi275 == 12:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 // _b41); _pc2 += 1
                elif _hi275 == 13:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 ** _b41); _pc2 += 1
                elif _hi275 == 14:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 ^ _b41); _pc2 += 1
                elif _hi275 == 15:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 & _b41); _pc2 += 1
                elif _hi275 == 16:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 | _b41); _pc2 += 1
                elif _hi275 == 17:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 << _b41); _pc2 += 1
                elif _hi275 == 18:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 >> _b41); _pc2 += 1
                elif _hi275 == 19:
                    _stk2.append(-_stk2.pop()); _pc2 += 1
                elif _hi275 == 20:
                    _stk2.append(~_stk2.pop()); _pc2 += 1
                elif _hi275 == 21:
                    _stk2.append(not _stk2.pop()); _pc2 += 1
                elif _hi275 == 22:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 == _b41); _pc2 += 1
                elif _hi275 == 23:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 != _b41); _pc2 += 1
                elif _hi275 == 24:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 < _b41); _pc2 += 1
                elif _hi275 == 25:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 > _b41); _pc2 += 1
                elif _hi275 == 26:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 <= _b41); _pc2 += 1
                elif _hi275 == 27:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 >= _b41); _pc2 += 1
                elif _hi275 == 28:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 is _b41); _pc2 += 1
                elif _hi275 == 29:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 in _b41); _pc2 += 1
                elif _hi275 == 30:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                elif _hi275 == 31:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if _stk2.pop() else _pc2 + 3
                elif _hi275 == 32:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if not _stk2.pop() else _pc2 + 3
                elif _hi275 == 33:
                    _tmp23 = _c2[_pc2+1]
                    if _tmp23: _val55 = _stk2[-_tmp23:]; del _stk2[-_tmp23:]
                    else: _val55 = []
                    _stk2.append(_stk2.pop()(*_val55)); _pc2 += 2
                elif _hi275 == 34:
                    _stk2.append(getattr(_stk2.pop(), _names39[_c2[_pc2+1]])); _pc2 += 2
                elif _hi275 == 35:
                    _val55 = _stk2.pop(); setattr(_stk2.pop(), _names39[_c2[_pc2+1]], _val55); _pc2 += 2
                elif _hi275 == 36:
                    _tmp23 = _c2[_pc2+2]
                    _val55 = [_stk2.pop() for _ in range(_tmp23)][::-1]
                    _stk2.append(getattr(_stk2.pop(), _names39[_c2[_pc2+1]])(*_val55)); _pc2 += 3
                elif _hi275 == 37:
                    _tmp23 = _c2[_pc2+1]
                    if _tmp23: _val55 = _stk2[-_tmp23:]; del _stk2[-_tmp23:]
                    else: _val55 = []
                    _stk2.append(_val55); _pc2 += 2
                elif _hi275 == 38:
                    _tmp23 = _c2[_pc2+1]
                    if _tmp23: _val55 = tuple(_stk2[-_tmp23:]); del _stk2[-_tmp23:]
                    else: _val55 = ()
                    _stk2.append(_val55); _pc2 += 2
                elif _hi275 == 39:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96[_b41]); _pc2 += 1
                elif _hi275 == 40:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _val55 = _stk2.pop(); _a96[_b41] = _val55; _pc2 += 1
                elif _hi275 == 41:
                    _val55 = list(_stk2.pop())[:_c2[_pc2+1]]; _stk2.extend(reversed(_val55)); _pc2 += 2
                elif _hi275 == 42:
                    _tmp23 = _c2[_pc2+1]; _val55 = {}
                    for _ in range(_tmp23): _b41 = _stk2.pop(); _a96 = _stk2.pop(); _val55[_a96] = _b41
                    _stk2.append(_val55); _pc2 += 2
                elif _hi275 == 43:
                    _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(slice(_a96, _b41)); _pc2 += 1
                elif _hi275 == 44:
                    _stk2.append(iter(_stk2.pop())); _pc2 += 1
                elif _hi275 == 45:
                    _val55 = next(_stk2[-1], None)
                    if _val55 is None: _stk2.pop(); _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                    else: _stk2.append(_val55); _pc2 += 3
                elif _hi275 == 46:
                    return _stk2.pop()
                elif _hi275 == 47:
                    _eh2.append(_c2[_pc2+1] | (_c2[_pc2+2] << 8)); _pc2 += 3
                elif _hi275 == 48:
                    _eh2.pop(); _pc2 += 1
                elif _hi275 == 49:
                    _tmp23 = _c2[_pc2+1] | (_c2[_pc2+2] << 8); _c2[_tmp23] ^= _c2[_pc2+3]; _pc2 += 4
                elif _hi275 == 50:
                    _regs2[_c2[_pc2+1]] = _loc36[_c2[_pc2+2]]; _pc2 += 3
                elif _hi275 == 51:
                    _loc36[_c2[_pc2+2]] = _regs2[_c2[_pc2+1]]; _pc2 += 3
                elif _hi275 == 52:
                    _stk2.append(_regs2[_c2[_pc2+1]]); _pc2 += 2
                elif _hi275 == 53:
                    _regs2[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _hi275 == 54:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] + _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _hi275 == 55:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] - _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _hi275 == 56:
                    _shared70[_c2[_pc2+1]].append(_stk2.pop()); _pc2 += 2
                elif _hi275 == 57:
                    _stk2.append(_shared70[_c2[_pc2+1]].pop()); _pc2 += 2
                elif _hi275 == 58:
                    _gregs41[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _hi275 == 59:
                    _stk2.append(_gregs41[_c2[_pc2+1]]); _pc2 += 2
                elif _hi275 == 60:
                    _pc2 += 1; break
                elif _hi275 == 61:
                    _stk2.append(_loc36[_c2[_pc2+1]]); _b41 = _stk2.pop(); _a96 = _stk2.pop(); _stk2.append(_a96 + _b41); _pc2 += 2
                elif _hi275 == 62:
                    _pc2 += 1
                elif _hi275 == 63:
                    return _stk2[-1] if _stk2 else None
                else: _pc2 += 1
              except Exception as _exc:
                if _eh2: _pc2 = _eh2.pop(); _stk2.append(_exc)
                else: raise
        elif _seg_vm37 == 3:
            _ic3 = 0
            while _pc3 < len(_c3):
              try:
                _ic3 += 1
                _op52 = _ot3[_c3[_pc3] & 0xFF]
                if _op52 == 1:
                    _stk3.append(_consts14[_c3[_pc3+1]]); _pc3 += 2
                elif _op52 == 2:
                    _stk3.append(_loc36[_c3[_pc3+1]]); _pc3 += 2
                elif _op52 == 3:
                    _loc36[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _op52 == 4:
                    _stk3.append(_gl31[_names39[_c3[_pc3+1]]]); _pc3 += 2
                elif _op52 == 5:
                    _gl31[_names39[_c3[_pc3+1]]] = _stk3.pop(); _pc3 += 2
                elif _op52 == 6:
                    _stk3.append(_stk3[-1]); _pc3 += 1
                elif _op52 == 7:
                    _stk3.pop(); _pc3 += 1
                elif _op52 == 8:
                    _stk3[-1], _stk3[-2] = _stk3[-2], _stk3[-1]; _pc3 += 1
                elif _op52 == 16:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 + _b41); _pc3 += 1
                elif _op52 == 17:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 - _b41); _pc3 += 1
                elif _op52 == 18:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 * _b41); _pc3 += 1
                elif _op52 == 19:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 % _b41); _pc3 += 1
                elif _op52 == 20:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 // _b41); _pc3 += 1
                elif _op52 == 21:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 ** _b41); _pc3 += 1
                elif _op52 == 22:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 ^ _b41); _pc3 += 1
                elif _op52 == 23:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 & _b41); _pc3 += 1
                elif _op52 == 24:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 | _b41); _pc3 += 1
                elif _op52 == 25:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 << _b41); _pc3 += 1
                elif _op52 == 26:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 >> _b41); _pc3 += 1
                elif _op52 == 32:
                    _stk3.append(-_stk3.pop()); _pc3 += 1
                elif _op52 == 33:
                    _stk3.append(~_stk3.pop()); _pc3 += 1
                elif _op52 == 34:
                    _stk3.append(not _stk3.pop()); _pc3 += 1
                elif _op52 == 48:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 == _b41); _pc3 += 1
                elif _op52 == 49:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 != _b41); _pc3 += 1
                elif _op52 == 50:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 < _b41); _pc3 += 1
                elif _op52 == 51:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 > _b41); _pc3 += 1
                elif _op52 == 52:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 <= _b41); _pc3 += 1
                elif _op52 == 53:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 >= _b41); _pc3 += 1
                elif _op52 == 54:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 is _b41); _pc3 += 1
                elif _op52 == 55:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 is not _b41); _pc3 += 1
                elif _op52 == 56:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 in _b41); _pc3 += 1
                elif _op52 == 64:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8))
                elif _op52 == 65:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8)) if _stk3.pop() else _pc3 + 3
                elif _op52 == 66:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8)) if not _stk3.pop() else _pc3 + 3
                elif _op52 == 80:
                    _tmp23 = _c3[_pc3+1]
                    if _tmp23: _val55 = _stk3[-_tmp23:]; del _stk3[-_tmp23:]
                    else: _val55 = []
                    _stk3.append(_stk3.pop()(*_val55)); _pc3 += 2
                elif _op52 == 81:
                    _stk3.append(getattr(_stk3.pop(), _names39[_c3[_pc3+1]])); _pc3 += 2
                elif _op52 == 82:
                    _val55 = _stk3.pop(); setattr(_stk3.pop(), _names39[_c3[_pc3+1]], _val55); _pc3 += 2
                elif _op52 == 83:
                    _tmp23 = _c3[_pc3+2]
                    _val55 = [_stk3.pop() for _ in range(_tmp23)][::-1]
                    _stk3.append(getattr(_stk3.pop(), _names39[_c3[_pc3+1]])(*_val55)); _pc3 += 3
                elif _op52 == 84:
                    _tmp23 = _c3[_pc3+1]
                    if _tmp23: _val55 = _stk3[-_tmp23:]; del _stk3[-_tmp23:]
                    else: _val55 = []
                    _stk3.append(_val55); _pc3 += 2
                elif _op52 == 85:
                    _tmp23 = _c3[_pc3+1]
                    if _tmp23: _val55 = tuple(_stk3[-_tmp23:]); del _stk3[-_tmp23:]
                    else: _val55 = ()
                    _stk3.append(_val55); _pc3 += 2
                elif _op52 == 86:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96[_b41]); _pc3 += 1
                elif _op52 == 87:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _val55 = _stk3.pop(); _a96[_b41] = _val55; _pc3 += 1
                elif _op52 == 88:
                    _val55 = list(_stk3.pop())[:_c3[_pc3+1]]; _stk3.extend(reversed(_val55)); _pc3 += 2
                elif _op52 == 89:
                    _tmp23 = _c3[_pc3+1]
                    _val55 = {}
                    for _ in range(_tmp23): _b41 = _stk3.pop(); _a96 = _stk3.pop(); _val55[_a96] = _b41
                    _stk3.append(_val55); _pc3 += 2
                elif _op52 == 90:
                    _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(slice(_a96, _b41)); _pc3 += 1
                elif _op52 == 96:
                    _stk3.append(iter(_stk3.pop())); _pc3 += 1
                elif _op52 == 97:
                    _val55 = next(_stk3[-1], None)
                    if _val55 is None: _stk3.pop(); _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8))
                    else: _stk3.append(_val55); _pc3 += 3
                elif _op52 == 112:
                    return _stk3.pop()
                elif _op52 == 120:
                    _eh3.append(_c3[_pc3+1] | (_c3[_pc3+2] << 8)); _pc3 += 3
                elif _op52 == 121:
                    _eh3.pop(); _pc3 += 1
                elif _op52 == 122:
                    _tmp23 = _c3[_pc3+1] | (_c3[_pc3+2] << 8); _c3[_tmp23] ^= _c3[_pc3+3]; _pc3 += 4
                elif _op52 == 128:
                    _regs3[_c3[_pc3+1]] = _loc36[_c3[_pc3+2]]; _pc3 += 3
                elif _op52 == 129:
                    _loc36[_c3[_pc3+2]] = _regs3[_c3[_pc3+1]]; _pc3 += 3
                elif _op52 == 130:
                    _stk3.append(_regs3[_c3[_pc3+1]]); _pc3 += 2
                elif _op52 == 131:
                    _regs3[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _op52 == 132:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _op52 == 133:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+1]] + _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _op52 == 134:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+1]] - _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _op52 == 144:
                    _shared70[_c3[_pc3+1]].append(_stk3.pop()); _pc3 += 2
                elif _op52 == 145:
                    _stk3.append(_shared70[_c3[_pc3+1]].pop()); _pc3 += 2
                elif _op52 == 146:
                    _gregs41[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _op52 == 147:
                    _stk3.append(_gregs41[_c3[_pc3+1]]); _pc3 += 2
                elif _op52 == 148:
                    _pc3 += 1; break
                elif _op52 == 160:
                    _loc36[_c3[_pc3+2]] = _consts14[_c3[_pc3+1]]; _pc3 += 3
                elif _op52 == 161:
                    _stk3.append(_loc36[_c3[_pc3+1]]); _b41 = _stk3.pop(); _a96 = _stk3.pop(); _stk3.append(_a96 + _b41); _pc3 += 2
                elif _op52 == 254:
                    _pc3 += 1
                elif _op52 == 255:
                    return _stk3[-1] if _stk3 else None
              except Exception as _exc:
                if _eh3: _pc3 = _eh3.pop(); _stk3.append(_exc)
                else: raise
        _hb95 = 0
        _hb95 = (_hb95 + len(_stk0) * 39) & 0xFFFF
        _hb95 = (_hb95 + len(_stk1) * 214) & 0xFFFF
        _hb95 = (_hb95 + len(_stk2) * 136) & 0xFFFF
        _hb95 = (_hb95 + len(_stk3) * 1) & 0xFFFF
        _hb95 = (_hb95 + _pc0 * 5) & 0xFFFF
        if len(_loc36) != 3: return None
        _si83 += 1
    return _stk0[-1] if _stk0 else None
def X10(*_args, **_kwargs):
    return _vm1802(*_args)

def _xn9234(_cs97):
    _r17 = (((((_cs97[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | ((_cs97[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF
    _tmp78 = (_cs97[1] << 17) & 0xFFFFFFFFFFFFFFFF
    _cs97[2] ^= _cs97[0]; _cs97[3] ^= _cs97[1]; _cs97[1] ^= _cs97[2]; _cs97[0] ^= _cs97[3]
    _cs97[2] ^= _tmp78; _cs97[3] = ((_cs97[3] << 45) | (_cs97[3] >> 19)) & 0xFFFFFFFFFFFFFFFF
    return _r17
def _xd9234(_v054, _v189, _k39):
    _delta77 = 0x9E3779B9; _s63 = (_delta77 * 32) & 0xFFFFFFFF
    for _ in range(32):
        _v189 = (_v189 - ((((_v054 << 4) ^ (_v054 >> 5)) + _v054) ^ (_s63 + _k39[(_s63 >> 11) & 3]))) & 0xFFFFFFFF
        _s63 = (_s63 - _delta77) & 0xFFFFFFFF
        _v054 = (_v054 - ((((_v189 << 4) ^ (_v189 >> 5)) + _v189) ^ (_s63 + _k39[_s63 & 3]))) & 0xFFFFFFFF
    return _v054, _v189
def _sh9234(_k39, _code14):
    _sv43 = [int.from_bytes(_k39[:8], 'little') ^ 0x736f6d6570736575, int.from_bytes(_k39[8:], 'little') ^ 0x646f72616e646f6d, int.from_bytes(_k39[:8], 'little') ^ 0x6c7967656e657261, int.from_bytes(_k39[8:], 'little') ^ 0x7465646279746573]
    def _sr():
        _sv43[0] = (_sv43[0] + _sv43[1]) & 0xFFFFFFFFFFFFFFFF; _sv43[1] = ((_sv43[1] << 13) | (_sv43[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ _sv43[0]; _sv43[0] = ((_sv43[0] << 32) | (_sv43[0] >> 32)) & 0xFFFFFFFFFFFFFFFF
        _sv43[2] = (_sv43[2] + _sv43[3]) & 0xFFFFFFFFFFFFFFFF; _sv43[3] = ((_sv43[3] << 16) | (_sv43[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ _sv43[2]
        _sv43[0] = (_sv43[0] + _sv43[3]) & 0xFFFFFFFFFFFFFFFF; _sv43[3] = ((_sv43[3] << 21) | (_sv43[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ _sv43[0]
        _sv43[2] = (_sv43[2] + _sv43[1]) & 0xFFFFFFFFFFFFFFFF; _sv43[1] = ((_sv43[1] << 17) | (_sv43[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ _sv43[2]; _sv43[2] = ((_sv43[2] << 32) | (_sv43[2] >> 32)) & 0xFFFFFFFFFFFFFFFF
    for _bi61 in range(0, len(_code14) - 7, 8):
        _tmp78 = int.from_bytes(_code14[_bi61:_bi61+8], 'little'); _sv43[3] ^= _tmp78; _sr(); _sr(); _sv43[0] ^= _tmp78
    _tmp78 = 0
    for _bi61 in range(len(_code14) & ~7, len(_code14)): _tmp78 |= _code14[_bi61] << (8 * (_bi61 & 7))
    _tmp78 |= (len(_code14) & 0xFF) << 56; _sv43[3] ^= _tmp78; _sr(); _sr(); _sv43[0] ^= _tmp78; _sv43[2] ^= 0xFF; _sr(); _sr(); _sr(); _sr()
    return (_sv43[0] ^ _sv43[1] ^ _sv43[2] ^ _sv43[3]) & 0xFFFFFFFFFFFFFFFF
def _vm9234(*_a18):
    _c1 = bytearray()
    _ek1 = (3940694632, 2959717694, 3992067646, 737395328)
    _ed1 = [11, 168, 167, 6, 91, 90, 69, 171, 235, 27, 221, 156, 138, 13, 174, 193, 127, 46, 242, 24, 178, 22, 187, 248, 166, 38, 151, 167, 39, 1, 164, 167, 62, 7, 126, 91, 206, 215, 5, 228, 77, 193, 47, 64, 195, 168, 133, 31, 24, 41, 198, 36, 162, 67, 114, 188, 228, 157, 64, 198, 74, 151, 196, 86, 9, 129, 77, 218, 32, 170, 97, 43]
    for _bi61 in range(0, len(_ed1), 8):
        _v054 = (_ed1[_bi61]<<24)|(_ed1[_bi61+1]<<16)|(_ed1[_bi61+2]<<8)|_ed1[_bi61+3]
        _v189 = (_ed1[_bi61+4]<<24)|(_ed1[_bi61+5]<<16)|(_ed1[_bi61+6]<<8)|_ed1[_bi61+7]
        _v054,_v189 = _xd9234(_v054,_v189,_ek1)
        _c1.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v189>>24)&0xFF,(_v189>>16)&0xFF,(_v189>>8)&0xFF,_v189&0xFF])
    _c1 = _c1[:71]
    if _sh9234(b'V\xb7y\xb1\xd4\n&\x08\xb5\x00\xb3\xa2\x87\xc9i\\', bytes(_c1)) != 6994453371474288670: raise MemoryError()
    _cs1 = [1368284567230730834, 14799482806419371669, 3863539730448083405, 4860960179587964594]
    for _bi61 in range(len(_c1)): _c1[_bi61] ^= _xn9234(_cs1) & 0xFF
    _c2 = bytearray()
    _ek2 = (3595620729, 922850877, 2430901356, 1955296321)
    _ed2 = [0, 79, 159, 217, 87, 6, 200, 20]
    for _bi61 in range(0, len(_ed2), 8):
        _v054 = (_ed2[_bi61]<<24)|(_ed2[_bi61+1]<<16)|(_ed2[_bi61+2]<<8)|_ed2[_bi61+3]
        _v189 = (_ed2[_bi61+4]<<24)|(_ed2[_bi61+5]<<16)|(_ed2[_bi61+6]<<8)|_ed2[_bi61+7]
        _v054,_v189 = _xd9234(_v054,_v189,_ek2)
        _c2.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v189>>24)&0xFF,(_v189>>16)&0xFF,(_v189>>8)&0xFF,_v189&0xFF])
    _c2 = _c2[:1]
    if _sh9234(b'V\xb7y\xb1\xd4\n&\x08\xb5\x00\xb3\xa2\x87\xc9i\\', bytes(_c2)) != 8396566722465053716: raise MemoryError()
    _cs2 = [10600840263796755292, 15364517024956863654, 7305856044031644076, 16095297659157096116]
    for _bi61 in range(len(_c2)): _c2[_bi61] ^= _xn9234(_cs2) & 0xFF
    _c4 = bytearray()
    _ek4 = (4168138581, 701981074, 3463845705, 2063655922)
    _ed4 = [212, 141, 118, 36, 49, 26, 188, 31, 217, 81, 134, 68, 199, 40, 183, 102, 95, 160, 11, 145, 52, 163, 251, 237]
    for _bi61 in range(0, len(_ed4), 8):
        _v054 = (_ed4[_bi61]<<24)|(_ed4[_bi61+1]<<16)|(_ed4[_bi61+2]<<8)|_ed4[_bi61+3]
        _v189 = (_ed4[_bi61+4]<<24)|(_ed4[_bi61+5]<<16)|(_ed4[_bi61+6]<<8)|_ed4[_bi61+7]
        _v054,_v189 = _xd9234(_v054,_v189,_ek4)
        _c4.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v189>>24)&0xFF,(_v189>>16)&0xFF,(_v189>>8)&0xFF,_v189&0xFF])
    _c0 = bytearray()
    _ek0 = (4270944087, 3385024536, 2602601177, 534481571)
    _ed0 = [135, 208, 92, 165, 190, 1, 193, 105]
    for _bi61 in range(0, len(_ed0), 8):
        _v054 = (_ed0[_bi61]<<24)|(_ed0[_bi61+1]<<16)|(_ed0[_bi61+2]<<8)|_ed0[_bi61+3]
        _v189 = (_ed0[_bi61+4]<<24)|(_ed0[_bi61+5]<<16)|(_ed0[_bi61+6]<<8)|_ed0[_bi61+7]
        _v054,_v189 = _xd9234(_v054,_v189,_ek0)
        _c0.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v189>>24)&0xFF,(_v189>>16)&0xFF,(_v189>>8)&0xFF,_v189&0xFF])
    _c0 = _c0[:5]
    if _sh9234(b'V\xb7y\xb1\xd4\n&\x08\xb5\x00\xb3\xa2\x87\xc9i\\', bytes(_c0)) != 8767678103193298613: raise MemoryError()
    _cs0 = [12135879813713971979, 8938476164241958753, 8524281123312356408, 816840338616865293]
    for _bi61 in range(len(_c0)): _c0[_bi61] ^= _xn9234(_cs0) & 0xFF
    _c5 = bytearray()
    _ek5 = (3389925373, 2806924749, 2607781100, 1938628882)
    _ed5 = [215, 208, 61, 47, 194, 71, 117, 1]
    for _bi61 in range(0, len(_ed5), 8):
        _v054 = (_ed5[_bi61]<<24)|(_ed5[_bi61+1]<<16)|(_ed5[_bi61+2]<<8)|_ed5[_bi61+3]
        _v189 = (_ed5[_bi61+4]<<24)|(_ed5[_bi61+5]<<16)|(_ed5[_bi61+6]<<8)|_ed5[_bi61+7]
        _v054,_v189 = _xd9234(_v054,_v189,_ek5)
        _c5.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v189>>24)&0xFF,(_v189>>16)&0xFF,(_v189>>8)&0xFF,_v189&0xFF])
    _c3 = bytearray()
    _ek3 = (1765155580, 2218974686, 79115368, 1030586504)
    _ed3 = [128, 156, 142, 34, 147, 183, 0, 114]
    for _bi61 in range(0, len(_ed3), 8):
        _v054 = (_ed3[_bi61]<<24)|(_ed3[_bi61+1]<<16)|(_ed3[_bi61+2]<<8)|_ed3[_bi61+3]
        _v189 = (_ed3[_bi61+4]<<24)|(_ed3[_bi61+5]<<16)|(_ed3[_bi61+6]<<8)|_ed3[_bi61+7]
        _v054,_v189 = _xd9234(_v054,_v189,_ek3)
        _c3.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v189>>24)&0xFF,(_v189>>16)&0xFF,(_v189>>8)&0xFF,_v189&0xFF])
    _c3 = _c3[:1]
    if _sh9234(b'V\xb7y\xb1\xd4\n&\x08\xb5\x00\xb3\xa2\x87\xc9i\\', bytes(_c3)) != 672970590850105204: raise MemoryError()
    _cs3 = [9651962449918775135, 514671169952176840, 3710263599296131157, 6956613144377515571]
    for _bi61 in range(len(_c3)): _c3[_bi61] ^= _xn9234(_cs3) & 0xFF
    _shared38 = [[] for _ in range(3)]
    _gregs53 = [None] * 4
    _loc78 = list(_a18[:1]) + [None] * 2
    _consts40 = [0, 3, 8867]
    _names22 = ['range']
    _gl52 = globals()
    _gl52.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))
    _ot0 = [78, 212, 191, 18, 204, 142, 65, 10, 23, 226, 146, 105, 253, 28, 48, 222, 243, 219, 136, 47, 118, 97, 185, 26, 201, 249, 252, 247, 45, 215, 55, 199, 84, 114, 62, 141, 63, 52, 167, 119, 5, 29, 190, 216, 38, 138, 121, 71, 19, 75, 151, 96, 95, 24, 240, 56, 206, 102, 140, 111, 169, 232, 57, 31, 177, 70, 175, 69, 164, 2, 203, 100, 4, 107, 211, 231, 67, 218, 21, 8, 207, 235, 238, 223, 233, 34, 101, 7, 108, 178, 91, 116, 35, 163, 170, 200, 0, 158, 139, 13, 39, 227, 225, 98, 176, 3, 188, 16, 194, 59, 245, 182, 246, 113, 90, 110, 61, 186, 32, 172, 94, 15, 80, 127, 40, 77, 230, 198, 193, 88, 189, 221, 208, 152, 99, 135, 128, 120, 234, 217, 147, 37, 17, 134, 51, 60, 237, 11, 150, 86, 229, 184, 242, 103, 210, 228, 25, 129, 14, 133, 174, 117, 54, 112, 20, 236, 72, 82, 195, 173, 46, 126, 168, 166, 1, 157, 213, 165, 49, 109, 183, 73, 79, 87, 220, 250, 85, 162, 44, 64, 145, 239, 132, 36, 196, 254, 42, 209, 205, 124, 43, 50, 22, 74, 179, 154, 130, 66, 155, 144, 192, 123, 171, 156, 106, 159, 93, 68, 89, 41, 181, 76, 149, 143, 251, 248, 30, 241, 148, 180, 9, 197, 6, 58, 202, 244, 160, 125, 255, 137, 161, 81, 224, 122, 115, 92, 33, 131, 53, 214, 104, 153, 83, 187, 27, 12]
    _stk0 = []
    _pc0 = 0
    _regs0 = [None] * 8
    _eh0 = []
    _ns0 = {}
    exec(bytes(b^205 for b in [169, 168, 171, 237, 146, 165, 171, 253, 146, 253, 229, 190, 225, 161, 225, 174, 225, 163, 225, 170, 225, 169, 225, 189, 225, 191, 225, 165, 225, 181, 228, 247, 199, 237, 175, 240, 190, 227, 189, 162, 189, 229, 228, 246, 172, 240, 190, 227, 189, 162, 189, 229, 228, 246, 190, 227, 172, 189, 189, 168, 163, 169, 229, 172, 240, 240, 175, 228, 246, 191, 168, 185, 184, 191, 163, 237, 189, 230, 252, 199, 169, 168, 171, 237, 146, 165, 171, 253, 146, 252, 229, 190, 225, 161, 225, 174, 225, 163, 225, 170, 225, 169, 225, 189, 225, 191, 225, 165, 225, 181, 228, 247, 199, 237, 190, 227, 172, 189, 189, 168, 163, 169, 229, 179, 190, 227, 189, 162, 189, 229, 228, 228, 246, 191, 168, 185, 184, 191, 163, 237, 189, 230, 252, 199, 169, 168, 171, 237, 146, 165, 171, 253, 146, 255, 229, 190, 225, 161, 225, 174, 225, 163, 225, 170, 225, 169, 225, 189, 225, 191, 225, 165, 225, 181, 228, 247, 199, 237, 161, 150, 169, 150, 189, 230, 252, 144, 144, 240, 190, 227, 189, 162, 189, 229, 228, 246, 191, 168, 185, 184, 191, 163, 237, 189, 230, 255, 199]).decode(),_ns0)
    _dh0 = {48: _ns0['_hf0_0'], 33: _ns0['_hf0_1'], 3: _ns0['_hf0_2']}
    _ot1 = [92, 200, 100, 177, 178, 135, 197, 110, 29, 250, 206, 228, 179, 160, 83, 150, 220, 173, 152, 238, 20, 58, 176, 66, 98, 225, 70, 115, 194, 144, 248, 46, 57, 201, 44, 231, 224, 148, 1, 74, 23, 199, 159, 55, 209, 165, 241, 80, 10, 217, 168, 164, 53, 234, 34, 12, 214, 68, 56, 243, 120, 7, 151, 149, 111, 249, 61, 198, 117, 136, 123, 105, 99, 63, 32, 247, 190, 229, 235, 119, 5, 143, 240, 16, 121, 213, 186, 134, 79, 219, 30, 133, 175, 11, 84, 109, 210, 208, 2, 242, 156, 155, 171, 112, 252, 50, 3, 25, 102, 71, 60, 245, 18, 21, 191, 251, 67, 64, 230, 130, 124, 246, 122, 193, 52, 161, 196, 77, 158, 146, 180, 211, 126, 97, 222, 31, 129, 8, 108, 62, 96, 167, 33, 15, 237, 85, 137, 216, 86, 73, 22, 170, 236, 91, 38, 17, 14, 43, 128, 255, 188, 19, 125, 132, 154, 4, 174, 28, 81, 47, 215, 75, 182, 189, 163, 94, 232, 103, 227, 140, 157, 35, 254, 192, 82, 142, 185, 203, 65, 48, 24, 42, 183, 253, 138, 93, 162, 76, 78, 207, 244, 127, 45, 69, 118, 59, 9, 184, 226, 131, 27, 39, 233, 6, 49, 113, 202, 90, 153, 169, 107, 166, 205, 26, 187, 145, 221, 88, 89, 218, 36, 212, 106, 72, 114, 181, 51, 139, 147, 116, 223, 195, 40, 239, 204, 104, 87, 101, 172, 54, 41, 37, 13, 141, 0, 95]
    _stk1 = []
    _pc1 = 0
    _regs1 = [None] * 8
    _eh1 = []
    _ns1 = {}
    exec(bytes(b^175 for b in [203, 202, 201, 143, 240, 199, 201, 158, 240, 159, 135, 220, 131, 195, 131, 204, 131, 193, 131, 200, 131, 203, 131, 223, 131, 221, 131, 199, 131, 215, 134, 149, 165, 143, 220, 129, 206, 223, 223, 202, 193, 203, 135, 220, 244, 130, 158, 242, 134, 148, 221, 202, 219, 218, 221, 193, 143, 223, 132, 158, 165, 203, 202, 201, 143, 240, 199, 201, 158, 240, 158, 135, 220, 131, 195, 131, 204, 131, 193, 131, 200, 131, 203, 131, 223, 131, 221, 131, 199, 131, 215, 134, 149, 165, 143, 220, 129, 206, 223, 223, 202, 193, 203, 135, 209, 220, 129, 223, 192, 223, 135, 134, 134, 148, 221, 202, 219, 218, 221, 193, 143, 223, 132, 158, 165, 203, 202, 201, 143, 240, 199, 201, 158, 240, 157, 135, 220, 131, 195, 131, 204, 131, 193, 131, 200, 131, 203, 131, 223, 131, 221, 131, 199, 131, 215, 134, 149, 165, 143, 220, 129, 206, 223, 223, 202, 193, 203, 135, 200, 244, 193, 244, 203, 244, 223, 132, 158, 242, 242, 242, 134, 148, 221, 202, 219, 218, 221, 193, 143, 223, 132, 157, 165, 203, 202, 201, 143, 240, 199, 201, 158, 240, 156, 135, 220, 131, 195, 131, 204, 131, 193, 131, 200, 131, 203, 131, 223, 131, 221, 131, 199, 131, 215, 134, 149, 165, 143, 220, 129, 206, 223, 223, 202, 193, 203, 135, 195, 244, 203, 244, 223, 132, 158, 242, 242, 134, 148, 221, 202, 219, 218, 221, 193, 143, 223, 132, 157, 165, 203, 202, 201, 143, 240, 199, 201, 158, 240, 155, 135, 220, 131, 195, 131, 204, 131, 193, 131, 200, 131, 203, 131, 223, 131, 221, 131, 199, 131, 215, 134, 149, 165, 143, 195, 244, 203, 244, 223, 132, 158, 242, 242, 146, 220, 129, 223, 192, 223, 135, 134, 148, 221, 202, 219, 218, 221, 193, 143, 223, 132, 157, 165]).decode(),_ns1)
    _dh1 = {6: _ns1['_hf1_0'], 33: _ns1['_hf1_1'], 4: _ns1['_hf1_2'], 2: _ns1['_hf1_3'], 3: _ns1['_hf1_4']}
    _ot2 = [249, 100, 56, 36, 118, 144, 238, 138, 0, 16, 208, 183, 113, 81, 179, 35, 209, 40, 132, 104, 24, 12, 173, 154, 34, 225, 152, 112, 187, 47, 180, 88, 186, 61, 39, 127, 64, 192, 1, 52, 135, 69, 145, 194, 7, 246, 123, 216, 240, 237, 90, 136, 235, 55, 22, 37, 167, 110, 177, 245, 17, 84, 195, 197, 147, 19, 196, 205, 82, 255, 131, 68, 185, 45, 243, 9, 57, 156, 27, 242, 161, 247, 133, 91, 181, 126, 76, 63, 222, 119, 207, 70, 151, 79, 4, 211, 253, 226, 109, 59, 49, 166, 121, 129, 83, 214, 254, 146, 210, 217, 116, 125, 42, 141, 137, 75, 163, 94, 10, 218, 102, 248, 33, 172, 206, 149, 213, 6, 85, 165, 241, 25, 236, 60, 65, 171, 43, 155, 139, 101, 176, 72, 15, 53, 107, 99, 193, 51, 198, 13, 41, 202, 199, 175, 230, 48, 103, 97, 157, 234, 114, 188, 143, 80, 169, 117, 2, 28, 93, 54, 134, 128, 200, 21, 239, 38, 232, 182, 231, 3, 251, 252, 77, 66, 203, 223, 162, 184, 96, 5, 11, 227, 233, 95, 250, 212, 108, 106, 74, 8, 111, 30, 124, 150, 160, 190, 158, 89, 122, 92, 178, 221, 201, 148, 219, 87, 215, 73, 174, 244, 189, 168, 204, 20, 78, 142, 164, 98, 23, 140, 58, 220, 71, 67, 120, 46, 26, 115, 130, 86, 14, 44, 29, 18, 105, 153, 170, 50, 228, 229, 62, 31, 224, 32, 159, 191]
    _stk2 = []
    _pc2 = 0
    _regs2 = [None] * 8
    _eh2 = []
    _dh2 = {}
    _ot3 = [221, 196, 168, 78, 217, 240, 173, 43, 81, 94, 25, 208, 103, 24, 35, 7, 129, 16, 128, 145, 214, 152, 223, 176, 64, 28, 133, 102, 69, 66, 44, 67, 49, 126, 135, 182, 62, 115, 231, 241, 84, 6, 4, 58, 199, 224, 101, 157, 164, 137, 48, 3, 193, 250, 54, 237, 5, 83, 226, 65, 246, 106, 34, 89, 139, 71, 98, 76, 27, 212, 42, 181, 85, 146, 211, 205, 79, 130, 73, 255, 60, 151, 105, 253, 187, 8, 53, 161, 87, 150, 138, 247, 242, 23, 235, 118, 116, 80, 112, 177, 30, 96, 124, 0, 143, 202, 9, 238, 178, 254, 170, 200, 169, 188, 197, 191, 144, 213, 233, 38, 167, 225, 244, 252, 229, 147, 90, 209, 153, 123, 195, 184, 127, 19, 140, 61, 114, 165, 13, 159, 148, 55, 216, 11, 183, 218, 56, 122, 50, 45, 93, 88, 134, 15, 248, 251, 172, 29, 194, 198, 18, 26, 104, 37, 219, 72, 131, 20, 220, 189, 111, 41, 74, 245, 95, 158, 204, 185, 142, 40, 52, 149, 77, 59, 39, 236, 160, 36, 109, 1, 156, 12, 180, 2, 234, 47, 97, 227, 108, 120, 206, 70, 92, 100, 22, 110, 17, 136, 31, 21, 125, 186, 154, 99, 68, 75, 201, 86, 132, 232, 163, 107, 192, 175, 46, 210, 190, 249, 171, 155, 228, 119, 239, 207, 203, 166, 63, 162, 222, 57, 215, 32, 117, 174, 91, 121, 141, 33, 113, 243, 51, 230, 179, 10, 14, 82]
    _stk3 = []
    _pc3 = 0
    _regs3 = [None] * 8
    _eh3 = []
    _dh3 = {}
    _tc33 = __import__('time').perf_counter_ns
    _segs = [(0, 1), (1, 6)]
    _tprev = _tc33()
    _ck91 = [2, 26]
    _si45 = 0
    for _seg_vm66, _seg_n72 in _segs:
        _td59 = _tc33() - _tprev
        if _td59 > 5000000000: return None
        _tprev = _tc33()
        if _seg_vm66 == 0:
            _ic0 = 0
            while _pc0 < len(_c0):
              try:
                _ic0 += 1
                _op91 = _ot0[_c0[_pc0] & 0xFF]
                if _op91 in _dh0:
                    _pc0 = _dh0[_op91](_stk0, _loc78, _consts40, _names22, _gl52, _c0, _pc0, _regs0, _shared38, _gregs53)
                    continue
                _dt019 = {1: 0, 2: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 16: 7, 17: 8, 18: 9, 19: 10, 20: 11, 21: 12, 22: 13, 23: 14, 24: 15, 25: 16, 26: 17, 32: 18, 34: 19, 49: 20, 50: 21, 51: 22, 52: 23, 53: 24, 54: 25, 55: 26, 56: 27, 64: 28, 65: 29, 66: 30, 80: 31, 81: 32, 82: 33, 83: 34, 84: 35, 85: 36, 86: 37, 87: 38, 88: 39, 89: 40, 90: 41, 96: 42, 97: 43, 112: 44, 120: 45, 121: 46, 122: 47, 128: 48, 129: 49, 130: 50, 131: 51, 132: 52, 133: 53, 134: 54, 144: 55, 145: 56, 146: 57, 147: 58, 148: 59, 160: 60, 161: 61, 254: 62, 255: 63}
                _hi071 = _dt019.get(_op91, -1)
                if _hi071 == 0:
                    _stk0.append(_consts40[_c0[_pc0+1]]); _pc0 += 2
                elif _hi071 == 1:
                    _stk0.append(_loc78[_c0[_pc0+1]]); _pc0 += 2
                elif _hi071 == 2:
                    _stk0.append(_gl52[_names22[_c0[_pc0+1]]]); _pc0 += 2
                elif _hi071 == 3:
                    _gl52[_names22[_c0[_pc0+1]]] = _stk0.pop(); _pc0 += 2
                elif _hi071 == 4:
                    _stk0.append(_stk0[-1]); _pc0 += 1
                elif _hi071 == 5:
                    _stk0.pop(); _pc0 += 1
                elif _hi071 == 6:
                    _stk0[-1], _stk0[-2] = _stk0[-2], _stk0[-1]; _pc0 += 1
                elif _hi071 == 7:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 + _b83); _pc0 += 1
                elif _hi071 == 8:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 - _b83); _pc0 += 1
                elif _hi071 == 9:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 * _b83); _pc0 += 1
                elif _hi071 == 10:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 % _b83); _pc0 += 1
                elif _hi071 == 11:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 // _b83); _pc0 += 1
                elif _hi071 == 12:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 ** _b83); _pc0 += 1
                elif _hi071 == 13:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 ^ _b83); _pc0 += 1
                elif _hi071 == 14:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 & _b83); _pc0 += 1
                elif _hi071 == 15:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 | _b83); _pc0 += 1
                elif _hi071 == 16:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 << _b83); _pc0 += 1
                elif _hi071 == 17:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 >> _b83); _pc0 += 1
                elif _hi071 == 18:
                    _stk0.append(-_stk0.pop()); _pc0 += 1
                elif _hi071 == 19:
                    _stk0.append(not _stk0.pop()); _pc0 += 1
                elif _hi071 == 20:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 != _b83); _pc0 += 1
                elif _hi071 == 21:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 < _b83); _pc0 += 1
                elif _hi071 == 22:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 > _b83); _pc0 += 1
                elif _hi071 == 23:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 <= _b83); _pc0 += 1
                elif _hi071 == 24:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 >= _b83); _pc0 += 1
                elif _hi071 == 25:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 is _b83); _pc0 += 1
                elif _hi071 == 26:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 is not _b83); _pc0 += 1
                elif _hi071 == 27:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 in _b83); _pc0 += 1
                elif _hi071 == 28:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                elif _hi071 == 29:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if _stk0.pop() else _pc0 + 3
                elif _hi071 == 30:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if not _stk0.pop() else _pc0 + 3
                elif _hi071 == 31:
                    _tmp78 = _c0[_pc0+1]
                    if _tmp78: _val10 = _stk0[-_tmp78:]; del _stk0[-_tmp78:]
                    else: _val10 = []
                    _stk0.append(_stk0.pop()(*_val10)); _pc0 += 2
                elif _hi071 == 32:
                    _stk0.append(getattr(_stk0.pop(), _names22[_c0[_pc0+1]])); _pc0 += 2
                elif _hi071 == 33:
                    _val10 = _stk0.pop(); setattr(_stk0.pop(), _names22[_c0[_pc0+1]], _val10); _pc0 += 2
                elif _hi071 == 34:
                    _tmp78 = _c0[_pc0+2]
                    _val10 = [_stk0.pop() for _ in range(_tmp78)][::-1]
                    _stk0.append(getattr(_stk0.pop(), _names22[_c0[_pc0+1]])(*_val10)); _pc0 += 3
                elif _hi071 == 35:
                    _tmp78 = _c0[_pc0+1]
                    if _tmp78: _val10 = _stk0[-_tmp78:]; del _stk0[-_tmp78:]
                    else: _val10 = []
                    _stk0.append(_val10); _pc0 += 2
                elif _hi071 == 36:
                    _tmp78 = _c0[_pc0+1]
                    if _tmp78: _val10 = tuple(_stk0[-_tmp78:]); del _stk0[-_tmp78:]
                    else: _val10 = ()
                    _stk0.append(_val10); _pc0 += 2
                elif _hi071 == 37:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18[_b83]); _pc0 += 1
                elif _hi071 == 38:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _val10 = _stk0.pop(); _a18[_b83] = _val10; _pc0 += 1
                elif _hi071 == 39:
                    _val10 = list(_stk0.pop())[:_c0[_pc0+1]]; _stk0.extend(reversed(_val10)); _pc0 += 2
                elif _hi071 == 40:
                    _tmp78 = _c0[_pc0+1]; _val10 = {}
                    for _ in range(_tmp78): _b83 = _stk0.pop(); _a18 = _stk0.pop(); _val10[_a18] = _b83
                    _stk0.append(_val10); _pc0 += 2
                elif _hi071 == 41:
                    _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(slice(_a18, _b83)); _pc0 += 1
                elif _hi071 == 42:
                    _stk0.append(iter(_stk0.pop())); _pc0 += 1
                elif _hi071 == 43:
                    _val10 = next(_stk0[-1], None)
                    if _val10 is None: _stk0.pop(); _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                    else: _stk0.append(_val10); _pc0 += 3
                elif _hi071 == 44:
                    return _stk0.pop()
                elif _hi071 == 45:
                    _eh0.append(_c0[_pc0+1] | (_c0[_pc0+2] << 8)); _pc0 += 3
                elif _hi071 == 46:
                    _eh0.pop(); _pc0 += 1
                elif _hi071 == 47:
                    _tmp78 = _c0[_pc0+1] | (_c0[_pc0+2] << 8); _c0[_tmp78] ^= _c0[_pc0+3]; _pc0 += 4
                elif _hi071 == 48:
                    _regs0[_c0[_pc0+1]] = _loc78[_c0[_pc0+2]]; _pc0 += 3
                elif _hi071 == 49:
                    _loc78[_c0[_pc0+2]] = _regs0[_c0[_pc0+1]]; _pc0 += 3
                elif _hi071 == 50:
                    _stk0.append(_regs0[_c0[_pc0+1]]); _pc0 += 2
                elif _hi071 == 51:
                    _regs0[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _hi071 == 52:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _hi071 == 53:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] + _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _hi071 == 54:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] - _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _hi071 == 55:
                    _shared38[_c0[_pc0+1]].append(_stk0.pop()); _pc0 += 2
                elif _hi071 == 56:
                    _stk0.append(_shared38[_c0[_pc0+1]].pop()); _pc0 += 2
                elif _hi071 == 57:
                    _gregs53[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _hi071 == 58:
                    _stk0.append(_gregs53[_c0[_pc0+1]]); _pc0 += 2
                elif _hi071 == 59:
                    _pc0 += 1; break
                elif _hi071 == 60:
                    _stk0.append(_loc78[_c0[_pc0+1]]); _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 + _b83); _pc0 += 2
                elif _hi071 == 61:
                    _stk0.append(_loc78[_c0[_pc0+1]]); _b83 = _stk0.pop(); _a18 = _stk0.pop(); _stk0.append(_a18 - _b83); _pc0 += 2
                elif _hi071 == 62:
                    _pc0 += 1
                elif _hi071 == 63:
                    return _stk0[-1] if _stk0 else None
                else: _pc0 += 1
              except Exception as _exc:
                if _eh0: _pc0 = _eh0.pop(); _stk0.append(_exc)
                else: raise
        elif _seg_vm66 == 1:
            _ic1 = 0
            while _pc1 < len(_c1):
              try:
                _ic1 += 1
                _op91 = _ot1[_c1[_pc1] & 0xFF]
                if _op91 in _dh1:
                    _pc1 = _dh1[_op91](_stk1, _loc78, _consts40, _names22, _gl52, _c1, _pc1, _regs1, _shared38, _gregs53)
                    continue
                _dt177 = {1: 0, 5: 1, 7: 2, 8: 3, 16: 4, 17: 5, 18: 6, 19: 7, 20: 8, 21: 9, 22: 10, 23: 11, 24: 12, 25: 13, 26: 14, 32: 15, 34: 16, 48: 17, 49: 18, 50: 19, 51: 20, 52: 21, 53: 22, 54: 23, 55: 24, 56: 25, 64: 26, 65: 27, 66: 28, 80: 29, 81: 30, 82: 31, 83: 32, 84: 33, 85: 34, 86: 35, 87: 36, 88: 37, 89: 38, 90: 39, 96: 40, 97: 41, 112: 42, 120: 43, 121: 44, 122: 45, 128: 46, 129: 47, 130: 48, 131: 49, 132: 50, 133: 51, 134: 52, 144: 53, 145: 54, 146: 55, 147: 56, 148: 57, 160: 58, 161: 59, 254: 60, 255: 61}
                _hi186 = _dt177.get(_op91, -1)
                if _hi186 == 0:
                    _stk1.append(_consts40[_c1[_pc1+1]]); _pc1 += 2
                elif _hi186 == 1:
                    _gl52[_names22[_c1[_pc1+1]]] = _stk1.pop(); _pc1 += 2
                elif _hi186 == 2:
                    _stk1.pop(); _pc1 += 1
                elif _hi186 == 3:
                    _stk1[-1], _stk1[-2] = _stk1[-2], _stk1[-1]; _pc1 += 1
                elif _hi186 == 4:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 + _b83); _pc1 += 1
                elif _hi186 == 5:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 - _b83); _pc1 += 1
                elif _hi186 == 6:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 * _b83); _pc1 += 1
                elif _hi186 == 7:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 % _b83); _pc1 += 1
                elif _hi186 == 8:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 // _b83); _pc1 += 1
                elif _hi186 == 9:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 ** _b83); _pc1 += 1
                elif _hi186 == 10:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 ^ _b83); _pc1 += 1
                elif _hi186 == 11:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 & _b83); _pc1 += 1
                elif _hi186 == 12:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 | _b83); _pc1 += 1
                elif _hi186 == 13:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 << _b83); _pc1 += 1
                elif _hi186 == 14:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 >> _b83); _pc1 += 1
                elif _hi186 == 15:
                    _stk1.append(-_stk1.pop()); _pc1 += 1
                elif _hi186 == 16:
                    _stk1.append(not _stk1.pop()); _pc1 += 1
                elif _hi186 == 17:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 == _b83); _pc1 += 1
                elif _hi186 == 18:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 != _b83); _pc1 += 1
                elif _hi186 == 19:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 < _b83); _pc1 += 1
                elif _hi186 == 20:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 > _b83); _pc1 += 1
                elif _hi186 == 21:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 <= _b83); _pc1 += 1
                elif _hi186 == 22:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 >= _b83); _pc1 += 1
                elif _hi186 == 23:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 is _b83); _pc1 += 1
                elif _hi186 == 24:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 is not _b83); _pc1 += 1
                elif _hi186 == 25:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 in _b83); _pc1 += 1
                elif _hi186 == 26:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                elif _hi186 == 27:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if _stk1.pop() else _pc1 + 3
                elif _hi186 == 28:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if not _stk1.pop() else _pc1 + 3
                elif _hi186 == 29:
                    _tmp78 = _c1[_pc1+1]
                    if _tmp78: _val10 = _stk1[-_tmp78:]; del _stk1[-_tmp78:]
                    else: _val10 = []
                    _stk1.append(_stk1.pop()(*_val10)); _pc1 += 2
                elif _hi186 == 30:
                    _stk1.append(getattr(_stk1.pop(), _names22[_c1[_pc1+1]])); _pc1 += 2
                elif _hi186 == 31:
                    _val10 = _stk1.pop(); setattr(_stk1.pop(), _names22[_c1[_pc1+1]], _val10); _pc1 += 2
                elif _hi186 == 32:
                    _tmp78 = _c1[_pc1+2]
                    _val10 = [_stk1.pop() for _ in range(_tmp78)][::-1]
                    _stk1.append(getattr(_stk1.pop(), _names22[_c1[_pc1+1]])(*_val10)); _pc1 += 3
                elif _hi186 == 33:
                    _tmp78 = _c1[_pc1+1]
                    if _tmp78: _val10 = _stk1[-_tmp78:]; del _stk1[-_tmp78:]
                    else: _val10 = []
                    _stk1.append(_val10); _pc1 += 2
                elif _hi186 == 34:
                    _tmp78 = _c1[_pc1+1]
                    if _tmp78: _val10 = tuple(_stk1[-_tmp78:]); del _stk1[-_tmp78:]
                    else: _val10 = ()
                    _stk1.append(_val10); _pc1 += 2
                elif _hi186 == 35:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18[_b83]); _pc1 += 1
                elif _hi186 == 36:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _val10 = _stk1.pop(); _a18[_b83] = _val10; _pc1 += 1
                elif _hi186 == 37:
                    _val10 = list(_stk1.pop())[:_c1[_pc1+1]]; _stk1.extend(reversed(_val10)); _pc1 += 2
                elif _hi186 == 38:
                    _tmp78 = _c1[_pc1+1]; _val10 = {}
                    for _ in range(_tmp78): _b83 = _stk1.pop(); _a18 = _stk1.pop(); _val10[_a18] = _b83
                    _stk1.append(_val10); _pc1 += 2
                elif _hi186 == 39:
                    _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(slice(_a18, _b83)); _pc1 += 1
                elif _hi186 == 40:
                    _stk1.append(iter(_stk1.pop())); _pc1 += 1
                elif _hi186 == 41:
                    _val10 = next(_stk1[-1], None)
                    if _val10 is None: _stk1.pop(); _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                    else: _stk1.append(_val10); _pc1 += 3
                elif _hi186 == 42:
                    return _stk1.pop()
                elif _hi186 == 43:
                    _eh1.append(_c1[_pc1+1] | (_c1[_pc1+2] << 8)); _pc1 += 3
                elif _hi186 == 44:
                    _eh1.pop(); _pc1 += 1
                elif _hi186 == 45:
                    _tmp78 = _c1[_pc1+1] | (_c1[_pc1+2] << 8); _c1[_tmp78] ^= _c1[_pc1+3]; _pc1 += 4
                elif _hi186 == 46:
                    _regs1[_c1[_pc1+1]] = _loc78[_c1[_pc1+2]]; _pc1 += 3
                elif _hi186 == 47:
                    _loc78[_c1[_pc1+2]] = _regs1[_c1[_pc1+1]]; _pc1 += 3
                elif _hi186 == 48:
                    _stk1.append(_regs1[_c1[_pc1+1]]); _pc1 += 2
                elif _hi186 == 49:
                    _regs1[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _hi186 == 50:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _hi186 == 51:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] + _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _hi186 == 52:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] - _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _hi186 == 53:
                    _shared38[_c1[_pc1+1]].append(_stk1.pop()); _pc1 += 2
                elif _hi186 == 54:
                    _stk1.append(_shared38[_c1[_pc1+1]].pop()); _pc1 += 2
                elif _hi186 == 55:
                    _gregs53[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _hi186 == 56:
                    _stk1.append(_gregs53[_c1[_pc1+1]]); _pc1 += 2
                elif _hi186 == 57:
                    _pc1 += 1; break
                elif _hi186 == 58:
                    _stk1.append(_loc78[_c1[_pc1+1]]); _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 + _b83); _pc1 += 2
                elif _hi186 == 59:
                    _stk1.append(_loc78[_c1[_pc1+1]]); _b83 = _stk1.pop(); _a18 = _stk1.pop(); _stk1.append(_a18 - _b83); _pc1 += 2
                elif _hi186 == 60:
                    _pc1 += 1
                elif _hi186 == 61:
                    return _stk1[-1] if _stk1 else None
                else: _pc1 += 1
              except Exception as _exc:
                if _eh1: _pc1 = _eh1.pop(); _stk1.append(_exc)
                else: raise
        elif _seg_vm66 == 2:
            _ic2 = 0
            while _pc2 < len(_c2):
              try:
                _ic2 += 1
                _op91 = _ot2[_c2[_pc2] & 0xFF]
                _ha283 = [255, 0, 1, 2, 3, 4, 5, 6, 7, 255, 255, 255, 255, 255, 255, 255, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 255, 255, 255, 255, 255, 19, 20, 21, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 22, 23, 24, 25, 26, 27, 28, 29, 30, 255, 255, 255, 255, 255, 255, 255, 31, 32, 33, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 255, 255, 255, 255, 255, 45, 46, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 47, 255, 255, 255, 255, 255, 255, 255, 48, 49, 50, 255, 255, 255, 255, 255, 51, 52, 53, 54, 55, 56, 57, 255, 255, 255, 255, 255, 255, 255, 255, 255, 58, 59, 60, 61, 62, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 64, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 65, 66]
                _ai284 = _ha283[_op91]
                if _ai284 == 0:
                    _stk2.append(_consts40[_c2[_pc2+1]]); _pc2 += 2
                elif _ai284 == 1:
                    _stk2.append(_loc78[_c2[_pc2+1]]); _pc2 += 2
                elif _ai284 == 2:
                    _loc78[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _ai284 == 3:
                    _stk2.append(_gl52[_names22[_c2[_pc2+1]]]); _pc2 += 2
                elif _ai284 == 4:
                    _gl52[_names22[_c2[_pc2+1]]] = _stk2.pop(); _pc2 += 2
                elif _ai284 == 5:
                    _stk2.append(_stk2[-1]); _pc2 += 1
                elif _ai284 == 6:
                    _stk2.pop(); _pc2 += 1
                elif _ai284 == 7:
                    _stk2[-1], _stk2[-2] = _stk2[-2], _stk2[-1]; _pc2 += 1
                elif _ai284 == 8:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 + _b83); _pc2 += 1
                elif _ai284 == 9:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 - _b83); _pc2 += 1
                elif _ai284 == 10:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 * _b83); _pc2 += 1
                elif _ai284 == 11:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 % _b83); _pc2 += 1
                elif _ai284 == 12:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 // _b83); _pc2 += 1
                elif _ai284 == 13:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 ** _b83); _pc2 += 1
                elif _ai284 == 14:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 ^ _b83); _pc2 += 1
                elif _ai284 == 15:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 & _b83); _pc2 += 1
                elif _ai284 == 16:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 | _b83); _pc2 += 1
                elif _ai284 == 17:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 << _b83); _pc2 += 1
                elif _ai284 == 18:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 >> _b83); _pc2 += 1
                elif _ai284 == 19:
                    _stk2.append(-_stk2.pop()); _pc2 += 1
                elif _ai284 == 20:
                    _stk2.append(~_stk2.pop()); _pc2 += 1
                elif _ai284 == 21:
                    _stk2.append(not _stk2.pop()); _pc2 += 1
                elif _ai284 == 22:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 == _b83); _pc2 += 1
                elif _ai284 == 23:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 != _b83); _pc2 += 1
                elif _ai284 == 24:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 < _b83); _pc2 += 1
                elif _ai284 == 25:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 > _b83); _pc2 += 1
                elif _ai284 == 26:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 <= _b83); _pc2 += 1
                elif _ai284 == 27:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 >= _b83); _pc2 += 1
                elif _ai284 == 28:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 is _b83); _pc2 += 1
                elif _ai284 == 29:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 is not _b83); _pc2 += 1
                elif _ai284 == 30:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 in _b83); _pc2 += 1
                elif _ai284 == 31:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                elif _ai284 == 32:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if _stk2.pop() else _pc2 + 3
                elif _ai284 == 33:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if not _stk2.pop() else _pc2 + 3
                elif _ai284 == 34:
                    _tmp78 = _c2[_pc2+1]
                    if _tmp78: _val10 = _stk2[-_tmp78:]; del _stk2[-_tmp78:]
                    else: _val10 = []
                    _stk2.append(_stk2.pop()(*_val10)); _pc2 += 2
                elif _ai284 == 35:
                    _stk2.append(getattr(_stk2.pop(), _names22[_c2[_pc2+1]])); _pc2 += 2
                elif _ai284 == 36:
                    _val10 = _stk2.pop(); setattr(_stk2.pop(), _names22[_c2[_pc2+1]], _val10); _pc2 += 2
                elif _ai284 == 37:
                    _tmp78 = _c2[_pc2+2]
                    _val10 = [_stk2.pop() for _ in range(_tmp78)][::-1]
                    _stk2.append(getattr(_stk2.pop(), _names22[_c2[_pc2+1]])(*_val10)); _pc2 += 3
                elif _ai284 == 38:
                    _tmp78 = _c2[_pc2+1]
                    if _tmp78: _val10 = _stk2[-_tmp78:]; del _stk2[-_tmp78:]
                    else: _val10 = []
                    _stk2.append(_val10); _pc2 += 2
                elif _ai284 == 39:
                    _tmp78 = _c2[_pc2+1]
                    if _tmp78: _val10 = tuple(_stk2[-_tmp78:]); del _stk2[-_tmp78:]
                    else: _val10 = ()
                    _stk2.append(_val10); _pc2 += 2
                elif _ai284 == 40:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18[_b83]); _pc2 += 1
                elif _ai284 == 41:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _val10 = _stk2.pop(); _a18[_b83] = _val10; _pc2 += 1
                elif _ai284 == 42:
                    _val10 = list(_stk2.pop())[:_c2[_pc2+1]]; _stk2.extend(reversed(_val10)); _pc2 += 2
                elif _ai284 == 43:
                    _tmp78 = _c2[_pc2+1]; _val10 = {}
                    for _ in range(_tmp78): _b83 = _stk2.pop(); _a18 = _stk2.pop(); _val10[_a18] = _b83
                    _stk2.append(_val10); _pc2 += 2
                elif _ai284 == 44:
                    _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(slice(_a18, _b83)); _pc2 += 1
                elif _ai284 == 45:
                    _stk2.append(iter(_stk2.pop())); _pc2 += 1
                elif _ai284 == 46:
                    _val10 = next(_stk2[-1], None)
                    if _val10 is None: _stk2.pop(); _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                    else: _stk2.append(_val10); _pc2 += 3
                elif _ai284 == 47:
                    return _stk2.pop()
                elif _ai284 == 48:
                    _eh2.append(_c2[_pc2+1] | (_c2[_pc2+2] << 8)); _pc2 += 3
                elif _ai284 == 49:
                    _eh2.pop(); _pc2 += 1
                elif _ai284 == 50:
                    _tmp78 = _c2[_pc2+1] | (_c2[_pc2+2] << 8); _c2[_tmp78] ^= _c2[_pc2+3]; _pc2 += 4
                elif _ai284 == 51:
                    _regs2[_c2[_pc2+1]] = _loc78[_c2[_pc2+2]]; _pc2 += 3
                elif _ai284 == 52:
                    _loc78[_c2[_pc2+2]] = _regs2[_c2[_pc2+1]]; _pc2 += 3
                elif _ai284 == 53:
                    _stk2.append(_regs2[_c2[_pc2+1]]); _pc2 += 2
                elif _ai284 == 54:
                    _regs2[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _ai284 == 55:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _ai284 == 56:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] + _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _ai284 == 57:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] - _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _ai284 == 58:
                    _shared38[_c2[_pc2+1]].append(_stk2.pop()); _pc2 += 2
                elif _ai284 == 59:
                    _stk2.append(_shared38[_c2[_pc2+1]].pop()); _pc2 += 2
                elif _ai284 == 60:
                    _gregs53[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _ai284 == 61:
                    _stk2.append(_gregs53[_c2[_pc2+1]]); _pc2 += 2
                elif _ai284 == 62:
                    _pc2 += 1; break
                elif _ai284 == 63:
                    _stk2.append(_loc78[_c2[_pc2+1]]); _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 + _b83); _pc2 += 2
                elif _ai284 == 64:
                    _stk2.append(_loc78[_c2[_pc2+1]]); _b83 = _stk2.pop(); _a18 = _stk2.pop(); _stk2.append(_a18 - _b83); _pc2 += 2
                elif _ai284 == 65:
                    _pc2 += 1
                elif _ai284 == 66:
                    return _stk2[-1] if _stk2 else None
                else: _pc2 += 1
              except Exception as _exc:
                if _eh2: _pc2 = _eh2.pop(); _stk2.append(_exc)
                else: raise
        elif _seg_vm66 == 3:
            _ic3 = 0
            while _pc3 < len(_c3):
              try:
                _ic3 += 1
                _op91 = _ot3[_c3[_pc3] & 0xFF]
                _ha373 = [255, 0, 1, 2, 3, 4, 5, 6, 7, 255, 255, 255, 255, 255, 255, 255, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 255, 255, 255, 255, 255, 19, 20, 21, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 22, 23, 24, 25, 26, 27, 28, 29, 30, 255, 255, 255, 255, 255, 255, 255, 31, 32, 33, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 255, 255, 255, 255, 255, 45, 46, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 47, 255, 255, 255, 255, 255, 255, 255, 48, 49, 50, 255, 255, 255, 255, 255, 51, 52, 53, 54, 55, 56, 57, 255, 255, 255, 255, 255, 255, 255, 255, 255, 58, 59, 60, 61, 62, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 64, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 65, 66]
                _ai321 = _ha373[_op91]
                if _ai321 == 0:
                    _stk3.append(_consts40[_c3[_pc3+1]]); _pc3 += 2
                elif _ai321 == 1:
                    _stk3.append(_loc78[_c3[_pc3+1]]); _pc3 += 2
                elif _ai321 == 2:
                    _loc78[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _ai321 == 3:
                    _stk3.append(_gl52[_names22[_c3[_pc3+1]]]); _pc3 += 2
                elif _ai321 == 4:
                    _gl52[_names22[_c3[_pc3+1]]] = _stk3.pop(); _pc3 += 2
                elif _ai321 == 5:
                    _stk3.append(_stk3[-1]); _pc3 += 1
                elif _ai321 == 6:
                    _stk3.pop(); _pc3 += 1
                elif _ai321 == 7:
                    _stk3[-1], _stk3[-2] = _stk3[-2], _stk3[-1]; _pc3 += 1
                elif _ai321 == 8:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 + _b83); _pc3 += 1
                elif _ai321 == 9:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 - _b83); _pc3 += 1
                elif _ai321 == 10:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 * _b83); _pc3 += 1
                elif _ai321 == 11:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 % _b83); _pc3 += 1
                elif _ai321 == 12:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 // _b83); _pc3 += 1
                elif _ai321 == 13:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 ** _b83); _pc3 += 1
                elif _ai321 == 14:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 ^ _b83); _pc3 += 1
                elif _ai321 == 15:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 & _b83); _pc3 += 1
                elif _ai321 == 16:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 | _b83); _pc3 += 1
                elif _ai321 == 17:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 << _b83); _pc3 += 1
                elif _ai321 == 18:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 >> _b83); _pc3 += 1
                elif _ai321 == 19:
                    _stk3.append(-_stk3.pop()); _pc3 += 1
                elif _ai321 == 20:
                    _stk3.append(~_stk3.pop()); _pc3 += 1
                elif _ai321 == 21:
                    _stk3.append(not _stk3.pop()); _pc3 += 1
                elif _ai321 == 22:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 == _b83); _pc3 += 1
                elif _ai321 == 23:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 != _b83); _pc3 += 1
                elif _ai321 == 24:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 < _b83); _pc3 += 1
                elif _ai321 == 25:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 > _b83); _pc3 += 1
                elif _ai321 == 26:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 <= _b83); _pc3 += 1
                elif _ai321 == 27:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 >= _b83); _pc3 += 1
                elif _ai321 == 28:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 is _b83); _pc3 += 1
                elif _ai321 == 29:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 is not _b83); _pc3 += 1
                elif _ai321 == 30:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 in _b83); _pc3 += 1
                elif _ai321 == 31:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8))
                elif _ai321 == 32:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8)) if _stk3.pop() else _pc3 + 3
                elif _ai321 == 33:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8)) if not _stk3.pop() else _pc3 + 3
                elif _ai321 == 34:
                    _tmp78 = _c3[_pc3+1]
                    if _tmp78: _val10 = _stk3[-_tmp78:]; del _stk3[-_tmp78:]
                    else: _val10 = []
                    _stk3.append(_stk3.pop()(*_val10)); _pc3 += 2
                elif _ai321 == 35:
                    _stk3.append(getattr(_stk3.pop(), _names22[_c3[_pc3+1]])); _pc3 += 2
                elif _ai321 == 36:
                    _val10 = _stk3.pop(); setattr(_stk3.pop(), _names22[_c3[_pc3+1]], _val10); _pc3 += 2
                elif _ai321 == 37:
                    _tmp78 = _c3[_pc3+2]
                    _val10 = [_stk3.pop() for _ in range(_tmp78)][::-1]
                    _stk3.append(getattr(_stk3.pop(), _names22[_c3[_pc3+1]])(*_val10)); _pc3 += 3
                elif _ai321 == 38:
                    _tmp78 = _c3[_pc3+1]
                    if _tmp78: _val10 = _stk3[-_tmp78:]; del _stk3[-_tmp78:]
                    else: _val10 = []
                    _stk3.append(_val10); _pc3 += 2
                elif _ai321 == 39:
                    _tmp78 = _c3[_pc3+1]
                    if _tmp78: _val10 = tuple(_stk3[-_tmp78:]); del _stk3[-_tmp78:]
                    else: _val10 = ()
                    _stk3.append(_val10); _pc3 += 2
                elif _ai321 == 40:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18[_b83]); _pc3 += 1
                elif _ai321 == 41:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _val10 = _stk3.pop(); _a18[_b83] = _val10; _pc3 += 1
                elif _ai321 == 42:
                    _val10 = list(_stk3.pop())[:_c3[_pc3+1]]; _stk3.extend(reversed(_val10)); _pc3 += 2
                elif _ai321 == 43:
                    _tmp78 = _c3[_pc3+1]; _val10 = {}
                    for _ in range(_tmp78): _b83 = _stk3.pop(); _a18 = _stk3.pop(); _val10[_a18] = _b83
                    _stk3.append(_val10); _pc3 += 2
                elif _ai321 == 44:
                    _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(slice(_a18, _b83)); _pc3 += 1
                elif _ai321 == 45:
                    _stk3.append(iter(_stk3.pop())); _pc3 += 1
                elif _ai321 == 46:
                    _val10 = next(_stk3[-1], None)
                    if _val10 is None: _stk3.pop(); _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8))
                    else: _stk3.append(_val10); _pc3 += 3
                elif _ai321 == 47:
                    return _stk3.pop()
                elif _ai321 == 48:
                    _eh3.append(_c3[_pc3+1] | (_c3[_pc3+2] << 8)); _pc3 += 3
                elif _ai321 == 49:
                    _eh3.pop(); _pc3 += 1
                elif _ai321 == 50:
                    _tmp78 = _c3[_pc3+1] | (_c3[_pc3+2] << 8); _c3[_tmp78] ^= _c3[_pc3+3]; _pc3 += 4
                elif _ai321 == 51:
                    _regs3[_c3[_pc3+1]] = _loc78[_c3[_pc3+2]]; _pc3 += 3
                elif _ai321 == 52:
                    _loc78[_c3[_pc3+2]] = _regs3[_c3[_pc3+1]]; _pc3 += 3
                elif _ai321 == 53:
                    _stk3.append(_regs3[_c3[_pc3+1]]); _pc3 += 2
                elif _ai321 == 54:
                    _regs3[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _ai321 == 55:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _ai321 == 56:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+1]] + _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _ai321 == 57:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+1]] - _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _ai321 == 58:
                    _shared38[_c3[_pc3+1]].append(_stk3.pop()); _pc3 += 2
                elif _ai321 == 59:
                    _stk3.append(_shared38[_c3[_pc3+1]].pop()); _pc3 += 2
                elif _ai321 == 60:
                    _gregs53[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _ai321 == 61:
                    _stk3.append(_gregs53[_c3[_pc3+1]]); _pc3 += 2
                elif _ai321 == 62:
                    _pc3 += 1; break
                elif _ai321 == 63:
                    _stk3.append(_loc78[_c3[_pc3+1]]); _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 + _b83); _pc3 += 2
                elif _ai321 == 64:
                    _stk3.append(_loc78[_c3[_pc3+1]]); _b83 = _stk3.pop(); _a18 = _stk3.pop(); _stk3.append(_a18 - _b83); _pc3 += 2
                elif _ai321 == 65:
                    _pc3 += 1
                elif _ai321 == 66:
                    return _stk3[-1] if _stk3 else None
                else: _pc3 += 1
              except Exception as _exc:
                if _eh3: _pc3 = _eh3.pop(); _stk3.append(_exc)
                else: raise
        _hb50 = 0
        _hb50 = (_hb50 + len(_stk0) * 28) & 0xFFFF
        _hb50 = (_hb50 + len(_stk1) * 216) & 0xFFFF
        _hb50 = (_hb50 + len(_stk2) * 133) & 0xFFFF
        _hb50 = (_hb50 + len(_stk3) * 96) & 0xFFFF
        _hb50 = (_hb50 + _pc0 * 69) & 0xFFFF
        if len(_loc78) != 3: return None
        _si45 += 1
    return _stk0[-1] if _stk0 else None
def X11(*_args, **_kwargs):
    return _vm9234(*_args)

def _xn1788(_cs91):
    _r72 = (((((_cs91[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | ((_cs91[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF
    _tmp22 = (_cs91[1] << 17) & 0xFFFFFFFFFFFFFFFF
    _cs91[2] ^= _cs91[0]; _cs91[3] ^= _cs91[1]; _cs91[1] ^= _cs91[2]; _cs91[0] ^= _cs91[3]
    _cs91[2] ^= _tmp22; _cs91[3] = ((_cs91[3] << 45) | (_cs91[3] >> 19)) & 0xFFFFFFFFFFFFFFFF
    return _r72
def _xd1788(_v030, _v144, _k12):
    _delta93 = 0x9E3779B9; _s41 = (_delta93 * 32) & 0xFFFFFFFF
    for _ in range(32):
        _v144 = (_v144 - ((((_v030 << 4) ^ (_v030 >> 5)) + _v030) ^ (_s41 + _k12[(_s41 >> 11) & 3]))) & 0xFFFFFFFF
        _s41 = (_s41 - _delta93) & 0xFFFFFFFF
        _v030 = (_v030 - ((((_v144 << 4) ^ (_v144 >> 5)) + _v144) ^ (_s41 + _k12[_s41 & 3]))) & 0xFFFFFFFF
    return _v030, _v144
def _sh1788(_k12, _code16):
    _sv41 = [int.from_bytes(_k12[:8], 'little') ^ 0x736f6d6570736575, int.from_bytes(_k12[8:], 'little') ^ 0x646f72616e646f6d, int.from_bytes(_k12[:8], 'little') ^ 0x6c7967656e657261, int.from_bytes(_k12[8:], 'little') ^ 0x7465646279746573]
    def _sr():
        _sv41[0] = (_sv41[0] + _sv41[1]) & 0xFFFFFFFFFFFFFFFF; _sv41[1] = ((_sv41[1] << 13) | (_sv41[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ _sv41[0]; _sv41[0] = ((_sv41[0] << 32) | (_sv41[0] >> 32)) & 0xFFFFFFFFFFFFFFFF
        _sv41[2] = (_sv41[2] + _sv41[3]) & 0xFFFFFFFFFFFFFFFF; _sv41[3] = ((_sv41[3] << 16) | (_sv41[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ _sv41[2]
        _sv41[0] = (_sv41[0] + _sv41[3]) & 0xFFFFFFFFFFFFFFFF; _sv41[3] = ((_sv41[3] << 21) | (_sv41[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ _sv41[0]
        _sv41[2] = (_sv41[2] + _sv41[1]) & 0xFFFFFFFFFFFFFFFF; _sv41[1] = ((_sv41[1] << 17) | (_sv41[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ _sv41[2]; _sv41[2] = ((_sv41[2] << 32) | (_sv41[2] >> 32)) & 0xFFFFFFFFFFFFFFFF
    for _bi11 in range(0, len(_code16) - 7, 8):
        _tmp22 = int.from_bytes(_code16[_bi11:_bi11+8], 'little'); _sv41[3] ^= _tmp22; _sr(); _sr(); _sv41[0] ^= _tmp22
    _tmp22 = 0
    for _bi11 in range(len(_code16) & ~7, len(_code16)): _tmp22 |= _code16[_bi11] << (8 * (_bi11 & 7))
    _tmp22 |= (len(_code16) & 0xFF) << 56; _sv41[3] ^= _tmp22; _sr(); _sr(); _sv41[0] ^= _tmp22; _sv41[2] ^= 0xFF; _sr(); _sr(); _sr(); _sr()
    return (_sv41[0] ^ _sv41[1] ^ _sv41[2] ^ _sv41[3]) & 0xFFFFFFFFFFFFFFFF
def _vm1788(*_a73):
    _c2 = bytearray()
    _ek2 = (450816914, 1783644280, 2993526976, 1693037913)
    _ed2 = [193, 77, 197, 173, 65, 233, 150, 152]
    for _bi11 in range(0, len(_ed2), 8):
        _v030 = (_ed2[_bi11]<<24)|(_ed2[_bi11+1]<<16)|(_ed2[_bi11+2]<<8)|_ed2[_bi11+3]
        _v144 = (_ed2[_bi11+4]<<24)|(_ed2[_bi11+5]<<16)|(_ed2[_bi11+6]<<8)|_ed2[_bi11+7]
        _v030,_v144 = _xd1788(_v030,_v144,_ek2)
        _c2.extend([(_v030>>24)&0xFF,(_v030>>16)&0xFF,(_v030>>8)&0xFF,_v030&0xFF,(_v144>>24)&0xFF,(_v144>>16)&0xFF,(_v144>>8)&0xFF,_v144&0xFF])
    _c2 = _c2[:1]
    if _sh1788(b'\xa0\xcb4\xf0\x0f\xd9\x9a-A\xa6.\xf6\xf7\xb1\xfd\xb1', bytes(_c2)) != 16183028915604655548: raise MemoryError()
    _cs2 = [3461198701828490907, 17516270126232185221, 4002997980628562198, 14062226193036652618]
    for _bi11 in range(len(_c2)): _c2[_bi11] ^= _xn1788(_cs2) & 0xFF
    _c0 = bytearray()
    _ek0 = (1859708092, 9115843, 762197539, 3368265728)
    _ed0 = [230, 9, 105, 179, 127, 239, 110, 101]
    for _bi11 in range(0, len(_ed0), 8):
        _v030 = (_ed0[_bi11]<<24)|(_ed0[_bi11+1]<<16)|(_ed0[_bi11+2]<<8)|_ed0[_bi11+3]
        _v144 = (_ed0[_bi11+4]<<24)|(_ed0[_bi11+5]<<16)|(_ed0[_bi11+6]<<8)|_ed0[_bi11+7]
        _v030,_v144 = _xd1788(_v030,_v144,_ek0)
        _c0.extend([(_v030>>24)&0xFF,(_v030>>16)&0xFF,(_v030>>8)&0xFF,_v030&0xFF,(_v144>>24)&0xFF,(_v144>>16)&0xFF,(_v144>>8)&0xFF,_v144&0xFF])
    _c0 = _c0[:5]
    if _sh1788(b'\xa0\xcb4\xf0\x0f\xd9\x9a-A\xa6.\xf6\xf7\xb1\xfd\xb1', bytes(_c0)) != 18080959523474621463: raise MemoryError()
    _cs0 = [1522140013112908102, 9766017256700848649, 8667087447466951732, 9528288109395682238]
    for _bi11 in range(len(_c0)): _c0[_bi11] ^= _xn1788(_cs0) & 0xFF
    _c3 = bytearray()
    _ek3 = (583266234, 2287054842, 3461809104, 1218153354)
    _ed3 = [78, 93, 10, 65, 67, 60, 116, 240, 101, 167, 96, 99, 160, 15, 118, 146]
    for _bi11 in range(0, len(_ed3), 8):
        _v030 = (_ed3[_bi11]<<24)|(_ed3[_bi11+1]<<16)|(_ed3[_bi11+2]<<8)|_ed3[_bi11+3]
        _v144 = (_ed3[_bi11+4]<<24)|(_ed3[_bi11+5]<<16)|(_ed3[_bi11+6]<<8)|_ed3[_bi11+7]
        _v030,_v144 = _xd1788(_v030,_v144,_ek3)
        _c3.extend([(_v030>>24)&0xFF,(_v030>>16)&0xFF,(_v030>>8)&0xFF,_v030&0xFF,(_v144>>24)&0xFF,(_v144>>16)&0xFF,(_v144>>8)&0xFF,_v144&0xFF])
    _c1 = bytearray()
    _ek1 = (3867355926, 2628775215, 824485607, 1525746147)
    _ed1 = [44, 29, 5, 253, 27, 127, 125, 45, 198, 221, 245, 126, 42, 242, 1, 143, 198, 237, 236, 57, 136, 194, 126, 232, 131, 237, 17, 127, 232, 189, 227, 122, 251, 175, 19, 30, 18, 48, 122, 51, 39, 182, 181, 190, 44, 23, 93, 175, 10, 115, 138, 228, 173, 133, 252, 183, 113, 228, 121, 175, 71, 46, 122, 137, 199, 202, 109, 229, 38, 98, 30, 219, 197, 181, 215, 251, 28, 143, 110, 249, 86, 142, 2, 7, 6, 199, 46, 252]
    for _bi11 in range(0, len(_ed1), 8):
        _v030 = (_ed1[_bi11]<<24)|(_ed1[_bi11+1]<<16)|(_ed1[_bi11+2]<<8)|_ed1[_bi11+3]
        _v144 = (_ed1[_bi11+4]<<24)|(_ed1[_bi11+5]<<16)|(_ed1[_bi11+6]<<8)|_ed1[_bi11+7]
        _v030,_v144 = _xd1788(_v030,_v144,_ek1)
        _c1.extend([(_v030>>24)&0xFF,(_v030>>16)&0xFF,(_v030>>8)&0xFF,_v030&0xFF,(_v144>>24)&0xFF,(_v144>>16)&0xFF,(_v144>>8)&0xFF,_v144&0xFF])
    _c1 = _c1[:87]
    if _sh1788(b'\xa0\xcb4\xf0\x0f\xd9\x9a-A\xa6.\xf6\xf7\xb1\xfd\xb1', bytes(_c1)) != 319781637272687133: raise MemoryError()
    _cs1 = [13523844010247403892, 10355672972055401429, 12297447368743595467, 7655239767984767488]
    for _bi11 in range(len(_c1)): _c1[_bi11] ^= _xn1788(_cs1) & 0xFF
    _shared29 = [[] for _ in range(2)]
    _gregs85 = [None] * 4
    _loc63 = list(_a73[:1]) + [None] * 3
    _consts23 = [0]
    _names75 = ['range']
    _gl46 = globals()
    _gl46.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))
    _ot0 = [156, 124, 149, 228, 249, 225, 26, 126, 134, 20, 57, 135, 190, 170, 142, 236, 13, 52, 127, 116, 185, 45, 112, 183, 175, 38, 128, 233, 10, 195, 120, 9, 243, 145, 8, 146, 246, 255, 98, 234, 129, 241, 150, 152, 35, 93, 251, 206, 12, 205, 200, 33, 198, 159, 85, 197, 143, 50, 194, 182, 81, 240, 88, 99, 82, 196, 111, 235, 213, 83, 208, 117, 132, 122, 89, 51, 169, 215, 223, 102, 242, 210, 204, 90, 59, 157, 115, 68, 151, 199, 30, 221, 224, 248, 114, 219, 173, 113, 64, 74, 4, 254, 17, 232, 160, 245, 176, 212, 105, 106, 86, 203, 125, 158, 94, 186, 110, 40, 91, 42, 187, 77, 32, 76, 25, 138, 209, 104, 107, 163, 0, 2, 130, 174, 5, 131, 46, 62, 184, 217, 165, 71, 78, 238, 75, 161, 216, 87, 39, 180, 72, 21, 43, 226, 101, 31, 211, 54, 166, 79, 103, 108, 55, 229, 44, 207, 177, 11, 140, 144, 237, 154, 67, 230, 155, 137, 73, 61, 164, 188, 191, 18, 70, 14, 178, 48, 181, 162, 1, 141, 253, 41, 49, 244, 123, 100, 16, 97, 218, 139, 118, 6, 56, 37, 60, 148, 28, 133, 189, 24, 84, 96, 192, 80, 23, 29, 201, 193, 7, 65, 63, 58, 231, 119, 121, 220, 147, 167, 136, 34, 202, 3, 36, 179, 27, 66, 95, 53, 239, 153, 250, 22, 15, 252, 247, 19, 109, 222, 227, 172, 47, 92, 171, 168, 214, 69]
    _stk0 = []
    _pc0 = 0
    _regs0 = [None] * 8
    _eh0 = []
    _ns0 = {}
    exec(bytes(b^238 for b in [138, 139, 136, 206, 177, 134, 136, 222, 177, 222, 198, 157, 194, 130, 194, 141, 194, 128, 194, 137, 194, 138, 194, 158, 194, 156, 194, 134, 194, 150, 199, 212, 228, 206, 140, 211, 157, 192, 158, 129, 158, 198, 199, 213, 143, 211, 157, 192, 158, 129, 158, 198, 199, 213, 157, 192, 143, 158, 158, 139, 128, 138, 198, 143, 207, 211, 140, 199, 213, 156, 139, 154, 155, 156, 128, 206, 158, 197, 223, 228, 138, 139, 136, 206, 177, 134, 136, 222, 177, 223, 198, 157, 194, 130, 194, 141, 194, 128, 194, 137, 194, 138, 194, 158, 194, 156, 194, 134, 194, 150, 199, 212, 228, 206, 157, 181, 195, 223, 179, 194, 157, 181, 195, 220, 179, 211, 157, 181, 195, 220, 179, 194, 157, 181, 195, 223, 179, 213, 156, 139, 154, 155, 156, 128, 206, 158, 197, 223, 228, 138, 139, 136, 206, 177, 134, 136, 222, 177, 220, 198, 157, 194, 130, 194, 141, 194, 128, 194, 137, 194, 138, 194, 158, 194, 156, 194, 134, 194, 150, 199, 212, 228, 206, 130, 181, 138, 181, 158, 197, 223, 179, 179, 211, 157, 192, 158, 129, 158, 198, 199, 213, 156, 139, 154, 155, 156, 128, 206, 158, 197, 220, 228]).decode(),_ns0)
    _dh0 = {49: _ns0['_hf0_0'], 8: _ns0['_hf0_1'], 3: _ns0['_hf0_2']}
    _ot1 = [153, 7, 71, 152, 59, 161, 113, 135, 2, 187, 149, 182, 167, 22, 233, 179, 49, 126, 209, 105, 248, 29, 210, 47, 9, 207, 252, 131, 25, 99, 203, 35, 89, 38, 190, 70, 184, 111, 61, 86, 208, 224, 177, 217, 91, 43, 1, 220, 116, 87, 6, 226, 55, 222, 50, 171, 46, 93, 163, 242, 10, 23, 129, 73, 185, 165, 56, 199, 21, 54, 118, 195, 114, 52, 108, 119, 3, 48, 12, 11, 223, 213, 172, 196, 155, 128, 246, 75, 41, 76, 244, 148, 69, 66, 219, 36, 160, 166, 214, 33, 122, 60, 193, 62, 241, 169, 243, 197, 84, 230, 106, 53, 90, 125, 123, 19, 150, 221, 80, 0, 143, 202, 96, 68, 156, 51, 176, 44, 146, 103, 225, 136, 249, 64, 42, 85, 100, 235, 157, 133, 120, 237, 181, 58, 77, 191, 4, 253, 231, 138, 174, 94, 144, 211, 112, 227, 151, 251, 63, 137, 95, 101, 205, 124, 154, 115, 141, 24, 79, 186, 107, 239, 13, 104, 98, 238, 34, 17, 82, 67, 109, 121, 97, 164, 18, 254, 168, 134, 200, 5, 127, 26, 183, 198, 162, 65, 216, 83, 130, 57, 81, 140, 194, 206, 228, 16, 45, 74, 30, 32, 255, 236, 180, 147, 110, 229, 145, 201, 188, 20, 204, 31, 170, 159, 173, 39, 234, 240, 212, 78, 117, 139, 40, 250, 8, 158, 92, 232, 102, 218, 132, 247, 27, 175, 189, 15, 178, 14, 142, 245, 215, 28, 37, 88, 72, 192]
    _stk1 = []
    _pc1 = 0
    _regs1 = [None] * 8
    _eh1 = []
    _ns1 = {}
    exec(bytes(b^38 for b in [66, 67, 64, 6, 121, 78, 64, 23, 121, 22, 14, 85, 10, 74, 10, 69, 10, 72, 10, 65, 10, 66, 10, 86, 10, 84, 10, 78, 10, 94, 15, 28, 44, 6, 68, 27, 85, 8, 86, 73, 86, 14, 15, 29, 71, 27, 85, 8, 86, 73, 86, 14, 15, 29, 85, 8, 71, 86, 86, 67, 72, 66, 14, 85, 74, 79, 69, 67, 14, 71, 10, 68, 15, 15, 29, 84, 67, 82, 83, 84, 72, 6, 86, 13, 23, 44, 66, 67, 64, 6, 121, 78, 64, 23, 121, 23, 14, 85, 10, 74, 10, 69, 10, 72, 10, 65, 10, 66, 10, 86, 10, 84, 10, 78, 10, 94, 15, 28, 44, 6, 68, 27, 85, 8, 86, 73, 86, 14, 15, 29, 71, 27, 85, 8, 86, 73, 86, 14, 15, 29, 85, 8, 71, 86, 86, 67, 72, 66, 14, 71, 27, 27, 68, 15, 29, 84, 67, 82, 83, 84, 72, 6, 86, 13, 23, 44, 66, 67, 64, 6, 121, 78, 64, 23, 121, 20, 14, 85, 10, 74, 10, 69, 10, 72, 10, 65, 10, 66, 10, 86, 10, 84, 10, 78, 10, 94, 15, 28, 44, 6, 85, 8, 71, 86, 86, 67, 72, 66, 14, 74, 125, 66, 125, 86, 13, 23, 123, 123, 15, 29, 84, 67, 82, 83, 84, 72, 6, 86, 13, 20, 44, 66, 67, 64, 6, 121, 78, 64, 23, 121, 21, 14, 85, 10, 74, 10, 69, 10, 72, 10, 65, 10, 66, 10, 86, 10, 84, 10, 78, 10, 94, 15, 28, 44, 6, 84, 125, 66, 125, 86, 13, 23, 123, 123, 27, 85, 8, 86, 73, 86, 14, 15, 29, 84, 67, 82, 83, 84, 72, 6, 86, 13, 20, 44, 66, 67, 64, 6, 121, 78, 64, 23, 121, 18, 14, 85, 10, 74, 10, 69, 10, 72, 10, 65, 10, 66, 10, 86, 10, 84, 10, 78, 10, 94, 15, 28, 44, 6, 85, 8, 71, 86, 86, 67, 72, 66, 14, 84, 125, 66, 125, 86, 13, 23, 123, 123, 15, 29, 84, 67, 82, 83, 84, 72, 6, 86, 13, 20, 44]).decode(),_ns1)
    _dh1 = {90: _ns1['_hf1_0'], 48: _ns1['_hf1_1'], 2: _ns1['_hf1_2'], 131: _ns1['_hf1_3'], 130: _ns1['_hf1_4']}
    _ot2 = [181, 160, 24, 227, 220, 194, 187, 153, 154, 90, 25, 129, 184, 151, 188, 87, 200, 148, 67, 22, 66, 203, 40, 234, 219, 161, 15, 141, 97, 112, 70, 215, 193, 132, 0, 168, 80, 33, 183, 69, 213, 96, 135, 45, 217, 14, 74, 253, 245, 222, 18, 11, 137, 98, 42, 38, 180, 43, 221, 211, 35, 145, 208, 113, 218, 32, 191, 83, 229, 51, 182, 246, 169, 93, 34, 174, 48, 62, 172, 50, 104, 131, 127, 167, 177, 140, 94, 226, 155, 79, 6, 209, 247, 244, 30, 68, 242, 248, 8, 101, 60, 86, 85, 224, 56, 210, 238, 147, 185, 252, 55, 241, 156, 205, 250, 1, 110, 157, 122, 178, 12, 21, 165, 158, 59, 117, 75, 73, 123, 232, 58, 65, 116, 144, 143, 92, 13, 142, 216, 197, 20, 189, 176, 108, 159, 76, 255, 236, 138, 41, 198, 44, 2, 84, 231, 228, 72, 149, 78, 99, 31, 212, 204, 201, 150, 190, 54, 89, 214, 239, 10, 81, 91, 121, 71, 249, 233, 23, 102, 163, 61, 82, 166, 106, 199, 207, 133, 251, 4, 254, 186, 63, 170, 9, 29, 49, 124, 100, 39, 111, 28, 192, 125, 225, 88, 27, 77, 3, 120, 36, 243, 179, 171, 64, 136, 103, 37, 195, 7, 95, 128, 53, 126, 107, 223, 240, 57, 130, 206, 119, 237, 19, 173, 115, 146, 202, 5, 162, 47, 16, 17, 164, 196, 118, 114, 230, 105, 235, 175, 26, 109, 134, 52, 139, 46, 152]
    _stk2 = []
    _pc2 = 0
    _regs2 = [None] * 8
    _eh2 = []
    _dh2 = {}
    _tc15 = __import__('time').perf_counter_ns
    _segs = [(0, 1), (1, 8)]
    _tprev = _tc15()
    _ck24 = [2, 33]
    _si98 = 0
    for _seg_vm51, _seg_n67 in _segs:
        _td52 = _tc15() - _tprev
        if _td52 > 5000000000: return None
        _tprev = _tc15()
        if _seg_vm51 == 0:
            _ic0 = 0
            while _pc0 < len(_c0):
              try:
                _ic0 += 1
                _op86 = _ot0[_c0[_pc0] & 0xFF]
                if _op86 in _dh0:
                    _pc0 = _dh0[_op86](_stk0, _loc63, _consts23, _names75, _gl46, _c0, _pc0, _regs0, _shared29, _gregs85)
                    continue
                if _op86 == 1:
                    _stk0.append(_consts23[_c0[_pc0+1]]); _pc0 += 2
                elif _op86 == 2:
                    _stk0.append(_loc63[_c0[_pc0+1]]); _pc0 += 2
                elif _op86 == 4:
                    _stk0.append(_gl46[_names75[_c0[_pc0+1]]]); _pc0 += 2
                elif _op86 == 5:
                    _gl46[_names75[_c0[_pc0+1]]] = _stk0.pop(); _pc0 += 2
                elif _op86 == 6:
                    _stk0.append(_stk0[-1]); _pc0 += 1
                elif _op86 == 7:
                    _stk0.pop(); _pc0 += 1
                elif _op86 == 16:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 + _b49); _pc0 += 1
                elif _op86 == 17:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 - _b49); _pc0 += 1
                elif _op86 == 18:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 * _b49); _pc0 += 1
                elif _op86 == 19:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 % _b49); _pc0 += 1
                elif _op86 == 20:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 // _b49); _pc0 += 1
                elif _op86 == 21:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 ** _b49); _pc0 += 1
                elif _op86 == 22:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 ^ _b49); _pc0 += 1
                elif _op86 == 23:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 & _b49); _pc0 += 1
                elif _op86 == 24:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 | _b49); _pc0 += 1
                elif _op86 == 25:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 << _b49); _pc0 += 1
                elif _op86 == 26:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 >> _b49); _pc0 += 1
                elif _op86 == 32:
                    _stk0.append(-_stk0.pop()); _pc0 += 1
                elif _op86 == 33:
                    _stk0.append(~_stk0.pop()); _pc0 += 1
                elif _op86 == 34:
                    _stk0.append(not _stk0.pop()); _pc0 += 1
                elif _op86 == 48:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 == _b49); _pc0 += 1
                elif _op86 == 50:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 < _b49); _pc0 += 1
                elif _op86 == 51:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 > _b49); _pc0 += 1
                elif _op86 == 52:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 <= _b49); _pc0 += 1
                elif _op86 == 53:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 >= _b49); _pc0 += 1
                elif _op86 == 54:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 is _b49); _pc0 += 1
                elif _op86 == 55:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 is not _b49); _pc0 += 1
                elif _op86 == 56:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 in _b49); _pc0 += 1
                elif _op86 == 64:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                elif _op86 == 65:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if _stk0.pop() else _pc0 + 3
                elif _op86 == 66:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if not _stk0.pop() else _pc0 + 3
                elif _op86 == 80:
                    _tmp22 = _c0[_pc0+1]
                    if _tmp22: _val30 = _stk0[-_tmp22:]; del _stk0[-_tmp22:]
                    else: _val30 = []
                    _stk0.append(_stk0.pop()(*_val30)); _pc0 += 2
                elif _op86 == 81:
                    _stk0.append(getattr(_stk0.pop(), _names75[_c0[_pc0+1]])); _pc0 += 2
                elif _op86 == 82:
                    _val30 = _stk0.pop(); setattr(_stk0.pop(), _names75[_c0[_pc0+1]], _val30); _pc0 += 2
                elif _op86 == 83:
                    _tmp22 = _c0[_pc0+2]
                    _val30 = [_stk0.pop() for _ in range(_tmp22)][::-1]
                    _stk0.append(getattr(_stk0.pop(), _names75[_c0[_pc0+1]])(*_val30)); _pc0 += 3
                elif _op86 == 84:
                    _tmp22 = _c0[_pc0+1]
                    if _tmp22: _val30 = _stk0[-_tmp22:]; del _stk0[-_tmp22:]
                    else: _val30 = []
                    _stk0.append(_val30); _pc0 += 2
                elif _op86 == 85:
                    _tmp22 = _c0[_pc0+1]
                    if _tmp22: _val30 = tuple(_stk0[-_tmp22:]); del _stk0[-_tmp22:]
                    else: _val30 = ()
                    _stk0.append(_val30); _pc0 += 2
                elif _op86 == 86:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73[_b49]); _pc0 += 1
                elif _op86 == 87:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _val30 = _stk0.pop(); _a73[_b49] = _val30; _pc0 += 1
                elif _op86 == 88:
                    _val30 = list(_stk0.pop())[:_c0[_pc0+1]]; _stk0.extend(reversed(_val30)); _pc0 += 2
                elif _op86 == 89:
                    _tmp22 = _c0[_pc0+1]
                    _val30 = {}
                    for _ in range(_tmp22): _b49 = _stk0.pop(); _a73 = _stk0.pop(); _val30[_a73] = _b49
                    _stk0.append(_val30); _pc0 += 2
                elif _op86 == 90:
                    _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(slice(_a73, _b49)); _pc0 += 1
                elif _op86 == 96:
                    _stk0.append(iter(_stk0.pop())); _pc0 += 1
                elif _op86 == 97:
                    _val30 = next(_stk0[-1], None)
                    if _val30 is None: _stk0.pop(); _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                    else: _stk0.append(_val30); _pc0 += 3
                elif _op86 == 112:
                    return _stk0.pop()
                elif _op86 == 120:
                    _eh0.append(_c0[_pc0+1] | (_c0[_pc0+2] << 8)); _pc0 += 3
                elif _op86 == 121:
                    _eh0.pop(); _pc0 += 1
                elif _op86 == 122:
                    _tmp22 = _c0[_pc0+1] | (_c0[_pc0+2] << 8); _c0[_tmp22] ^= _c0[_pc0+3]; _pc0 += 4
                elif _op86 == 128:
                    _regs0[_c0[_pc0+1]] = _loc63[_c0[_pc0+2]]; _pc0 += 3
                elif _op86 == 129:
                    _loc63[_c0[_pc0+2]] = _regs0[_c0[_pc0+1]]; _pc0 += 3
                elif _op86 == 130:
                    _stk0.append(_regs0[_c0[_pc0+1]]); _pc0 += 2
                elif _op86 == 131:
                    _regs0[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _op86 == 132:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _op86 == 133:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] + _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _op86 == 134:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] - _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _op86 == 144:
                    _shared29[_c0[_pc0+1]].append(_stk0.pop()); _pc0 += 2
                elif _op86 == 145:
                    _stk0.append(_shared29[_c0[_pc0+1]].pop()); _pc0 += 2
                elif _op86 == 146:
                    _gregs85[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _op86 == 147:
                    _stk0.append(_gregs85[_c0[_pc0+1]]); _pc0 += 2
                elif _op86 == 148:
                    _pc0 += 1; break
                elif _op86 == 160:
                    _stk0.append(_stk0[-1]); _loc63[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _op86 == 161:
                    _stk0.append(_loc63[_c0[_pc0+1]]); _b49 = _stk0.pop(); _a73 = _stk0.pop(); _stk0.append(_a73 + _b49); _pc0 += 2
                elif _op86 == 254:
                    _pc0 += 1
                elif _op86 == 255:
                    return _stk0[-1] if _stk0 else None
              except Exception as _exc:
                if _eh0: _pc0 = _eh0.pop(); _stk0.append(_exc)
                else: raise
        elif _seg_vm51 == 1:
            _ic1 = 0
            while _pc1 < len(_c1):
              try:
                _ic1 += 1
                _op86 = _ot1[_c1[_pc1] & 0xFF]
                if _op86 in _dh1:
                    _pc1 = _dh1[_op86](_stk1, _loc63, _consts23, _names75, _gl46, _c1, _pc1, _regs1, _shared29, _gregs85)
                    continue
                _dt147 = {1: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 16: 7, 17: 8, 18: 9, 19: 10, 20: 11, 21: 12, 22: 13, 23: 14, 24: 15, 25: 16, 26: 17, 32: 18, 33: 19, 34: 20, 49: 21, 50: 22, 51: 23, 52: 24, 53: 25, 54: 26, 55: 27, 56: 28, 64: 29, 65: 30, 66: 31, 80: 32, 81: 33, 82: 34, 83: 35, 84: 36, 85: 37, 86: 38, 87: 39, 88: 40, 89: 41, 96: 42, 97: 43, 112: 44, 120: 45, 121: 46, 122: 47, 128: 48, 129: 49, 132: 50, 133: 51, 134: 52, 144: 53, 145: 54, 146: 55, 147: 56, 148: 57, 160: 58, 161: 59, 254: 60, 255: 61}
                _hi157 = _dt147.get(_op86, -1)
                if _hi157 == 0:
                    _stk1.append(_consts23[_c1[_pc1+1]]); _pc1 += 2
                elif _hi157 == 1:
                    _loc63[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _hi157 == 2:
                    _stk1.append(_gl46[_names75[_c1[_pc1+1]]]); _pc1 += 2
                elif _hi157 == 3:
                    _gl46[_names75[_c1[_pc1+1]]] = _stk1.pop(); _pc1 += 2
                elif _hi157 == 4:
                    _stk1.append(_stk1[-1]); _pc1 += 1
                elif _hi157 == 5:
                    _stk1.pop(); _pc1 += 1
                elif _hi157 == 6:
                    _stk1[-1], _stk1[-2] = _stk1[-2], _stk1[-1]; _pc1 += 1
                elif _hi157 == 7:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 + _b49); _pc1 += 1
                elif _hi157 == 8:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 - _b49); _pc1 += 1
                elif _hi157 == 9:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 * _b49); _pc1 += 1
                elif _hi157 == 10:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 % _b49); _pc1 += 1
                elif _hi157 == 11:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 // _b49); _pc1 += 1
                elif _hi157 == 12:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 ** _b49); _pc1 += 1
                elif _hi157 == 13:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 ^ _b49); _pc1 += 1
                elif _hi157 == 14:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 & _b49); _pc1 += 1
                elif _hi157 == 15:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 | _b49); _pc1 += 1
                elif _hi157 == 16:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 << _b49); _pc1 += 1
                elif _hi157 == 17:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 >> _b49); _pc1 += 1
                elif _hi157 == 18:
                    _stk1.append(-_stk1.pop()); _pc1 += 1
                elif _hi157 == 19:
                    _stk1.append(~_stk1.pop()); _pc1 += 1
                elif _hi157 == 20:
                    _stk1.append(not _stk1.pop()); _pc1 += 1
                elif _hi157 == 21:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 != _b49); _pc1 += 1
                elif _hi157 == 22:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 < _b49); _pc1 += 1
                elif _hi157 == 23:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 > _b49); _pc1 += 1
                elif _hi157 == 24:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 <= _b49); _pc1 += 1
                elif _hi157 == 25:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 >= _b49); _pc1 += 1
                elif _hi157 == 26:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 is _b49); _pc1 += 1
                elif _hi157 == 27:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 is not _b49); _pc1 += 1
                elif _hi157 == 28:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 in _b49); _pc1 += 1
                elif _hi157 == 29:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                elif _hi157 == 30:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if _stk1.pop() else _pc1 + 3
                elif _hi157 == 31:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if not _stk1.pop() else _pc1 + 3
                elif _hi157 == 32:
                    _tmp22 = _c1[_pc1+1]
                    if _tmp22: _val30 = _stk1[-_tmp22:]; del _stk1[-_tmp22:]
                    else: _val30 = []
                    _stk1.append(_stk1.pop()(*_val30)); _pc1 += 2
                elif _hi157 == 33:
                    _stk1.append(getattr(_stk1.pop(), _names75[_c1[_pc1+1]])); _pc1 += 2
                elif _hi157 == 34:
                    _val30 = _stk1.pop(); setattr(_stk1.pop(), _names75[_c1[_pc1+1]], _val30); _pc1 += 2
                elif _hi157 == 35:
                    _tmp22 = _c1[_pc1+2]
                    _val30 = [_stk1.pop() for _ in range(_tmp22)][::-1]
                    _stk1.append(getattr(_stk1.pop(), _names75[_c1[_pc1+1]])(*_val30)); _pc1 += 3
                elif _hi157 == 36:
                    _tmp22 = _c1[_pc1+1]
                    if _tmp22: _val30 = _stk1[-_tmp22:]; del _stk1[-_tmp22:]
                    else: _val30 = []
                    _stk1.append(_val30); _pc1 += 2
                elif _hi157 == 37:
                    _tmp22 = _c1[_pc1+1]
                    if _tmp22: _val30 = tuple(_stk1[-_tmp22:]); del _stk1[-_tmp22:]
                    else: _val30 = ()
                    _stk1.append(_val30); _pc1 += 2
                elif _hi157 == 38:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73[_b49]); _pc1 += 1
                elif _hi157 == 39:
                    _b49 = _stk1.pop(); _a73 = _stk1.pop(); _val30 = _stk1.pop(); _a73[_b49] = _val30; _pc1 += 1
                elif _hi157 == 40:
                    _val30 = list(_stk1.pop())[:_c1[_pc1+1]]; _stk1.extend(reversed(_val30)); _pc1 += 2
                elif _hi157 == 41:
                    _tmp22 = _c1[_pc1+1]; _val30 = {}
                    for _ in range(_tmp22): _b49 = _stk1.pop(); _a73 = _stk1.pop(); _val30[_a73] = _b49
                    _stk1.append(_val30); _pc1 += 2
                elif _hi157 == 42:
                    _stk1.append(iter(_stk1.pop())); _pc1 += 1
                elif _hi157 == 43:
                    _val30 = next(_stk1[-1], None)
                    if _val30 is None: _stk1.pop(); _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                    else: _stk1.append(_val30); _pc1 += 3
                elif _hi157 == 44:
                    return _stk1.pop()
                elif _hi157 == 45:
                    _eh1.append(_c1[_pc1+1] | (_c1[_pc1+2] << 8)); _pc1 += 3
                elif _hi157 == 46:
                    _eh1.pop(); _pc1 += 1
                elif _hi157 == 47:
                    _tmp22 = _c1[_pc1+1] | (_c1[_pc1+2] << 8); _c1[_tmp22] ^= _c1[_pc1+3]; _pc1 += 4
                elif _hi157 == 48:
                    _regs1[_c1[_pc1+1]] = _loc63[_c1[_pc1+2]]; _pc1 += 3
                elif _hi157 == 49:
                    _loc63[_c1[_pc1+2]] = _regs1[_c1[_pc1+1]]; _pc1 += 3
                elif _hi157 == 50:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _hi157 == 51:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] + _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _hi157 == 52:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] - _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _hi157 == 53:
                    _shared29[_c1[_pc1+1]].append(_stk1.pop()); _pc1 += 2
                elif _hi157 == 54:
                    _stk1.append(_shared29[_c1[_pc1+1]].pop()); _pc1 += 2
                elif _hi157 == 55:
                    _gregs85[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _hi157 == 56:
                    _stk1.append(_gregs85[_c1[_pc1+1]]); _pc1 += 2
                elif _hi157 == 57:
                    _pc1 += 1; break
                elif _hi157 == 58:
                    _stk1.append(_stk1[-1]); _loc63[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _hi157 == 59:
                    _stk1.append(_loc63[_c1[_pc1+1]]); _b49 = _stk1.pop(); _a73 = _stk1.pop(); _stk1.append(_a73 + _b49); _pc1 += 2
                elif _hi157 == 60:
                    _pc1 += 1
                elif _hi157 == 61:
                    return _stk1[-1] if _stk1 else None
                else: _pc1 += 1
              except Exception as _exc:
                if _eh1: _pc1 = _eh1.pop(); _stk1.append(_exc)
                else: raise
        elif _seg_vm51 == 2:
            _ic2 = 0
            while _pc2 < len(_c2):
              try:
                _ic2 += 1
                _op86 = _ot2[_c2[_pc2] & 0xFF]
                if _op86 == 1:
                    _stk2.append(_consts23[_c2[_pc2+1]]); _pc2 += 2
                elif _op86 == 2:
                    _stk2.append(_loc63[_c2[_pc2+1]]); _pc2 += 2
                elif _op86 == 3:
                    _loc63[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _op86 == 4:
                    _stk2.append(_gl46[_names75[_c2[_pc2+1]]]); _pc2 += 2
                elif _op86 == 5:
                    _gl46[_names75[_c2[_pc2+1]]] = _stk2.pop(); _pc2 += 2
                elif _op86 == 6:
                    _stk2.append(_stk2[-1]); _pc2 += 1
                elif _op86 == 7:
                    _stk2.pop(); _pc2 += 1
                elif _op86 == 8:
                    _stk2[-1], _stk2[-2] = _stk2[-2], _stk2[-1]; _pc2 += 1
                elif _op86 == 16:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 + _b49); _pc2 += 1
                elif _op86 == 17:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 - _b49); _pc2 += 1
                elif _op86 == 18:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 * _b49); _pc2 += 1
                elif _op86 == 19:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 % _b49); _pc2 += 1
                elif _op86 == 20:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 // _b49); _pc2 += 1
                elif _op86 == 21:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 ** _b49); _pc2 += 1
                elif _op86 == 22:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 ^ _b49); _pc2 += 1
                elif _op86 == 23:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 & _b49); _pc2 += 1
                elif _op86 == 24:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 | _b49); _pc2 += 1
                elif _op86 == 25:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 << _b49); _pc2 += 1
                elif _op86 == 26:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 >> _b49); _pc2 += 1
                elif _op86 == 32:
                    _stk2.append(-_stk2.pop()); _pc2 += 1
                elif _op86 == 33:
                    _stk2.append(~_stk2.pop()); _pc2 += 1
                elif _op86 == 34:
                    _stk2.append(not _stk2.pop()); _pc2 += 1
                elif _op86 == 48:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 == _b49); _pc2 += 1
                elif _op86 == 49:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 != _b49); _pc2 += 1
                elif _op86 == 50:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 < _b49); _pc2 += 1
                elif _op86 == 51:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 > _b49); _pc2 += 1
                elif _op86 == 52:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 <= _b49); _pc2 += 1
                elif _op86 == 53:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 >= _b49); _pc2 += 1
                elif _op86 == 54:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 is _b49); _pc2 += 1
                elif _op86 == 55:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 is not _b49); _pc2 += 1
                elif _op86 == 56:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 in _b49); _pc2 += 1
                elif _op86 == 64:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                elif _op86 == 65:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if _stk2.pop() else _pc2 + 3
                elif _op86 == 66:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if not _stk2.pop() else _pc2 + 3
                elif _op86 == 80:
                    _tmp22 = _c2[_pc2+1]
                    if _tmp22: _val30 = _stk2[-_tmp22:]; del _stk2[-_tmp22:]
                    else: _val30 = []
                    _stk2.append(_stk2.pop()(*_val30)); _pc2 += 2
                elif _op86 == 81:
                    _stk2.append(getattr(_stk2.pop(), _names75[_c2[_pc2+1]])); _pc2 += 2
                elif _op86 == 82:
                    _val30 = _stk2.pop(); setattr(_stk2.pop(), _names75[_c2[_pc2+1]], _val30); _pc2 += 2
                elif _op86 == 83:
                    _tmp22 = _c2[_pc2+2]
                    _val30 = [_stk2.pop() for _ in range(_tmp22)][::-1]
                    _stk2.append(getattr(_stk2.pop(), _names75[_c2[_pc2+1]])(*_val30)); _pc2 += 3
                elif _op86 == 84:
                    _tmp22 = _c2[_pc2+1]
                    if _tmp22: _val30 = _stk2[-_tmp22:]; del _stk2[-_tmp22:]
                    else: _val30 = []
                    _stk2.append(_val30); _pc2 += 2
                elif _op86 == 85:
                    _tmp22 = _c2[_pc2+1]
                    if _tmp22: _val30 = tuple(_stk2[-_tmp22:]); del _stk2[-_tmp22:]
                    else: _val30 = ()
                    _stk2.append(_val30); _pc2 += 2
                elif _op86 == 86:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73[_b49]); _pc2 += 1
                elif _op86 == 87:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _val30 = _stk2.pop(); _a73[_b49] = _val30; _pc2 += 1
                elif _op86 == 88:
                    _val30 = list(_stk2.pop())[:_c2[_pc2+1]]; _stk2.extend(reversed(_val30)); _pc2 += 2
                elif _op86 == 89:
                    _tmp22 = _c2[_pc2+1]
                    _val30 = {}
                    for _ in range(_tmp22): _b49 = _stk2.pop(); _a73 = _stk2.pop(); _val30[_a73] = _b49
                    _stk2.append(_val30); _pc2 += 2
                elif _op86 == 90:
                    _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(slice(_a73, _b49)); _pc2 += 1
                elif _op86 == 96:
                    _stk2.append(iter(_stk2.pop())); _pc2 += 1
                elif _op86 == 97:
                    _val30 = next(_stk2[-1], None)
                    if _val30 is None: _stk2.pop(); _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                    else: _stk2.append(_val30); _pc2 += 3
                elif _op86 == 112:
                    return _stk2.pop()
                elif _op86 == 120:
                    _eh2.append(_c2[_pc2+1] | (_c2[_pc2+2] << 8)); _pc2 += 3
                elif _op86 == 121:
                    _eh2.pop(); _pc2 += 1
                elif _op86 == 122:
                    _tmp22 = _c2[_pc2+1] | (_c2[_pc2+2] << 8); _c2[_tmp22] ^= _c2[_pc2+3]; _pc2 += 4
                elif _op86 == 128:
                    _regs2[_c2[_pc2+1]] = _loc63[_c2[_pc2+2]]; _pc2 += 3
                elif _op86 == 129:
                    _loc63[_c2[_pc2+2]] = _regs2[_c2[_pc2+1]]; _pc2 += 3
                elif _op86 == 130:
                    _stk2.append(_regs2[_c2[_pc2+1]]); _pc2 += 2
                elif _op86 == 131:
                    _regs2[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _op86 == 132:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _op86 == 133:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] + _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _op86 == 134:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] - _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _op86 == 144:
                    _shared29[_c2[_pc2+1]].append(_stk2.pop()); _pc2 += 2
                elif _op86 == 145:
                    _stk2.append(_shared29[_c2[_pc2+1]].pop()); _pc2 += 2
                elif _op86 == 146:
                    _gregs85[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _op86 == 147:
                    _stk2.append(_gregs85[_c2[_pc2+1]]); _pc2 += 2
                elif _op86 == 148:
                    _pc2 += 1; break
                elif _op86 == 160:
                    _stk2.append(_stk2[-1]); _loc63[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _op86 == 161:
                    _stk2.append(_loc63[_c2[_pc2+1]]); _b49 = _stk2.pop(); _a73 = _stk2.pop(); _stk2.append(_a73 + _b49); _pc2 += 2
                elif _op86 == 254:
                    _pc2 += 1
                elif _op86 == 255:
                    return _stk2[-1] if _stk2 else None
              except Exception as _exc:
                if _eh2: _pc2 = _eh2.pop(); _stk2.append(_exc)
                else: raise
        _hb13 = 0
        _hb13 = (_hb13 + len(_stk0) * 228) & 0xFFFF
        _hb13 = (_hb13 + len(_stk1) * 22) & 0xFFFF
        _hb13 = (_hb13 + len(_stk2) * 149) & 0xFFFF
        _hb13 = (_hb13 + _pc0 * 113) & 0xFFFF
        if len(_loc63) != 4: return None
        _si98 += 1
    return _stk0[-1] if _stk0 else None
def X5(*_args, **_kwargs):
    return _vm1788(*_args)

def X3(*_a, **_k):
    if getattr(__import__(bytes([c ^ 26 for c in [105, 99, 105]]).decode()), bytes([c ^ 197 for c in [162, 160, 177, 177, 183, 164, 166, 160]]).decode())() or getattr(__import__(bytes([c ^ 26 for c in [105, 99, 105]]).decode()), bytes([c ^ 103 for c in [0, 2, 19, 23, 21, 8, 1, 14, 11, 2]]).decode())(): raise RecursionError()
    _d36 = b'zZ\x8ah\x96\x0eTe\x9f?\x1c\xf6\xacx\xf9p\xee"\xc4iz\xe0WC\x1e\xe0\xc9.\x84|\x08\xc5\xd3\x85\xdc\xf1(\x1b\xf6\x0cif\xfb\xe4A\xe5\x13>M\xad\xcc\xea\x11\xd7<\x93\x140m\'1W\xf4\x07\x02Vx\xd1\x15|\'\xe9~\x98\xb0\xc9 \x8a1\xc2&s\xb10\x9a\xdf\nN\xf0\x1b\x9b\x01\xb1\x80\xfa\x8b\xdcu\xb6\x89\xe0\xeb\x92g*K\xf7\xf7\xcc\xe7SH\xf4xw\xa8)\tF\xe0\xdf\xdd\x83\x91\x12\xce\x16\xbd[\xcf\xf5\x90c\xe5;G\xd7\xbc\xbe&\xb82Zk[&l\x8a;\xc0\xd2T6\x03\x08C\xae\x0c\x0e\xf7\x1c\xb3\x0f\x9dF\xa6\x88\\G\xf7v\'a\x7f\xf0\x1d\xf1m\xf6\xc2\xe5\x1fp?\xfb\x04\x96W\xf9\x85\x96\xf6\x97\x16L\t\xfb\xd9 \xdc\x17\x82\x9f\x12_\x96\xb6\xec\xbd\x85({dVY\x94(\xf9D\xf1\xb6!y\xd7n+\x9f\x8a\xd3\xb6\x16] \xf0\xc5\\\x96"\xe3tT\xd5\x02\xf9\xab\xe6\x9e\xad\xd3a\xc1nJ'
    _sf190 = 13221566747450194150
    _fo27 = 401041644 ^ 2533094697
    _fp89 = 226828596 ^ 210051239
    _cm58 = 15052731810360093406 ^ 9851624156606043635
    _kg88 = 9622181871719661957 ^ 1999495807959022992
    _ks73 = 1583530390520400126 ^ 4937375893340488299
    _kb60 = 10453752835147657078 ^ 18094010533426079358
    _sf286 = 6410024282364189987
    _q150 = 12879520
    _salt98 = _sf190 ^ _sf286
    _n91 = len(_d36)
    _s169 = (_salt98 * _kg88 + _n91) & 18446744073709551615
    _s243 = (_salt98 ^ (_n91 * _ks73)) & 18446744073709551615
    _s381 = (_s169 ^ _s243 ^ _kb60) & 18446744073709551615
    _q275 = _s169 & 0xFF
    _hv30 = _fo27
    for _bi53 in _d36:
        _hv30 = ((_hv30 ^ _bi53) * _fp89) & 0xFFFFFFFF
    if _hv30 != 2030923847:
        _d36 = b'\x00'
        raise RecursionError()
    _out87 = bytearray(_n91)
    _st60 = _s169
    _ic21 = _s243 | 1
    for _pos19 in range(0, _n91, 4):
        _o64 = _st60
        _st60 = (_o64 * _cm58 + _ic21) & 18446744073709551615
        _x25 = (((_o64 >> 18) ^ _o64) >> 27) & 0xFFFFFFFF
        _r30 = (_o64 >> 59) & 0x1F
        _val32 = ((_x25 >> _r30) | (_x25 << (32 - _r30))) & 0xFFFFFFFF
        for _sh93 in range(min(4, _n91 - _pos19)):
            _out87[_pos19 + _sh93] = _d36[_pos19 + _sh93] ^ ((_val32 >> (_sh93 * 8)) & 0xFF)
    _pm51 = list(range(_n91))
    _st60 = _s381
    _ic21 = (_s381 >> 32) | 1
    for _j60 in range(_n91 - 1, 0, -1):
        _o64 = _st60
        _st60 = (_o64 * _cm58 + _ic21) & 18446744073709551615
        _x25 = (((_o64 >> 18) ^ _o64) >> 27) & 0xFFFFFFFF
        _r30 = (_o64 >> 59) & 0x1F
        _idx36 = ((_x25 >> _r30) | (_x25 << (32 - _r30))) & 0xFFFFFFFF
        _idx36 = _idx36 % (_j60 + 1)
        _pm51[_j60], _pm51[_idx36] = _pm51[_idx36], _pm51[_j60]
    _up87 = bytearray(_n91)
    for _j60 in range(_n91):
        _up87[_j60] = _out87[_pm51[_j60]]
    _q334 = _pm51[0] ^ _q275
    _m = __import__(bytes([c ^ 167 for c in [202, 198, 213, 212, 207, 198, 203]]).decode())
    _t = __import__(bytes([c ^ 28 for c in [104, 101, 108, 121, 111]]).decode())
    _co88 = _m.loads(bytes(_up87))
    _kw55 = {'co_filename': '<>', 'co_name': '<>'}
    if hasattr(_co88, bytes([c ^ 90 for c in [57, 53, 5, 43, 47, 59, 54, 52, 59, 55, 63]]).decode()): _kw55[bytes([c ^ 90 for c in [57, 53, 5, 43, 47, 59, 54, 52, 59, 55, 63]]).decode()] = '<>'
    _co88 = _co88.replace(**_kw55)
    _f57 = getattr(_t, bytes([c ^ 218 for c in [156, 175, 180, 185, 174, 179, 181, 180, 142, 163, 170, 191]]).decode())(_co88, globals(), None, None)
    _f57.__kwdefaults__ = None
    _q410 = _q334 + _q150
    _d36 = b'\x00'
    _up87 = b'\x00'
    _out87 = b'\x00'
    _ak21 = bytes([c ^ 252 for c in [163, 163, 159, 147, 152, 153, 163, 163]]).decode()
    setattr(X3, _ak21, getattr(_f57, _ak21))
    _ak21 = bytes([c ^ 16 for c in [79, 79, 116, 117, 118, 113, 101, 124, 100, 99, 79, 79]]).decode()
    setattr(X3, _ak21, getattr(_f57, _ak21))
    _ak21 = bytes([c ^ 87 for c in [8, 8, 60, 32, 51, 50, 49, 54, 34, 59, 35, 36, 8, 8]]).decode()
    setattr(X3, _ak21, getattr(_f57, _ak21))
    _q544 = _q410 ^ len(_ak21)
    return _f57(*_a, **_k)
def _xn4512(_cs88):
    _r93 = (((((_cs88[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | ((_cs88[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF
    _tmp50 = (_cs88[1] << 17) & 0xFFFFFFFFFFFFFFFF
    _cs88[2] ^= _cs88[0]; _cs88[3] ^= _cs88[1]; _cs88[1] ^= _cs88[2]; _cs88[0] ^= _cs88[3]
    _cs88[2] ^= _tmp50; _cs88[3] = ((_cs88[3] << 45) | (_cs88[3] >> 19)) & 0xFFFFFFFFFFFFFFFF
    return _r93
def _xd4512(_v054, _v159, _k87):
    _delta44 = 0x9E3779B9; _s40 = (_delta44 * 32) & 0xFFFFFFFF
    for _ in range(32):
        _v159 = (_v159 - ((((_v054 << 4) ^ (_v054 >> 5)) + _v054) ^ (_s40 + _k87[(_s40 >> 11) & 3]))) & 0xFFFFFFFF
        _s40 = (_s40 - _delta44) & 0xFFFFFFFF
        _v054 = (_v054 - ((((_v159 << 4) ^ (_v159 >> 5)) + _v159) ^ (_s40 + _k87[_s40 & 3]))) & 0xFFFFFFFF
    return _v054, _v159
def _sh4512(_k87, _code89):
    _sv31 = [int.from_bytes(_k87[:8], 'little') ^ 0x736f6d6570736575, int.from_bytes(_k87[8:], 'little') ^ 0x646f72616e646f6d, int.from_bytes(_k87[:8], 'little') ^ 0x6c7967656e657261, int.from_bytes(_k87[8:], 'little') ^ 0x7465646279746573]
    def _sr():
        _sv31[0] = (_sv31[0] + _sv31[1]) & 0xFFFFFFFFFFFFFFFF; _sv31[1] = ((_sv31[1] << 13) | (_sv31[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ _sv31[0]; _sv31[0] = ((_sv31[0] << 32) | (_sv31[0] >> 32)) & 0xFFFFFFFFFFFFFFFF
        _sv31[2] = (_sv31[2] + _sv31[3]) & 0xFFFFFFFFFFFFFFFF; _sv31[3] = ((_sv31[3] << 16) | (_sv31[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ _sv31[2]
        _sv31[0] = (_sv31[0] + _sv31[3]) & 0xFFFFFFFFFFFFFFFF; _sv31[3] = ((_sv31[3] << 21) | (_sv31[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ _sv31[0]
        _sv31[2] = (_sv31[2] + _sv31[1]) & 0xFFFFFFFFFFFFFFFF; _sv31[1] = ((_sv31[1] << 17) | (_sv31[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ _sv31[2]; _sv31[2] = ((_sv31[2] << 32) | (_sv31[2] >> 32)) & 0xFFFFFFFFFFFFFFFF
    for _bi95 in range(0, len(_code89) - 7, 8):
        _tmp50 = int.from_bytes(_code89[_bi95:_bi95+8], 'little'); _sv31[3] ^= _tmp50; _sr(); _sr(); _sv31[0] ^= _tmp50
    _tmp50 = 0
    for _bi95 in range(len(_code89) & ~7, len(_code89)): _tmp50 |= _code89[_bi95] << (8 * (_bi95 & 7))
    _tmp50 |= (len(_code89) & 0xFF) << 56; _sv31[3] ^= _tmp50; _sr(); _sr(); _sv31[0] ^= _tmp50; _sv31[2] ^= 0xFF; _sr(); _sr(); _sr(); _sr()
    return (_sv31[0] ^ _sv31[1] ^ _sv31[2] ^ _sv31[3]) & 0xFFFFFFFFFFFFFFFF
def _vm4512(*_a70):
    _c4 = bytearray()
    _ek4 = (2081849195, 267078707, 3919048948, 4120174636)
    _ed4 = [237, 198, 228, 204, 162, 0, 146, 194, 225, 32, 48, 130, 70, 94, 245, 139]
    for _bi95 in range(0, len(_ed4), 8):
        _v054 = (_ed4[_bi95]<<24)|(_ed4[_bi95+1]<<16)|(_ed4[_bi95+2]<<8)|_ed4[_bi95+3]
        _v159 = (_ed4[_bi95+4]<<24)|(_ed4[_bi95+5]<<16)|(_ed4[_bi95+6]<<8)|_ed4[_bi95+7]
        _v054,_v159 = _xd4512(_v054,_v159,_ek4)
        _c4.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v159>>24)&0xFF,(_v159>>16)&0xFF,(_v159>>8)&0xFF,_v159&0xFF])
    _c0 = bytearray()
    _ek0 = (2406783754, 3995969049, 2470516863, 2594788344)
    _ed0 = [194, 34, 214, 229, 150, 48, 56, 214, 82, 25, 43, 68, 73, 72, 181, 203, 126, 88, 7, 23, 217, 202, 188, 213]
    for _bi95 in range(0, len(_ed0), 8):
        _v054 = (_ed0[_bi95]<<24)|(_ed0[_bi95+1]<<16)|(_ed0[_bi95+2]<<8)|_ed0[_bi95+3]
        _v159 = (_ed0[_bi95+4]<<24)|(_ed0[_bi95+5]<<16)|(_ed0[_bi95+6]<<8)|_ed0[_bi95+7]
        _v054,_v159 = _xd4512(_v054,_v159,_ek0)
        _c0.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v159>>24)&0xFF,(_v159>>16)&0xFF,(_v159>>8)&0xFF,_v159&0xFF])
    _c0 = _c0[:18]
    if _sh4512(b'\xc4 \x93n\xdf\xb4.\xaa\xa6t\xd1\x0f\xf9Q4;', bytes(_c0)) != 3690860302778351611: raise MemoryError()
    _cs0 = [10450463985543339876, 8316001990546540023, 7641167535253396049, 6228189088265663860]
    for _bi95 in range(len(_c0)): _c0[_bi95] ^= _xn4512(_cs0) & 0xFF
    _c2 = bytearray()
    _ek2 = (705678671, 289929174, 3060091126, 536584845)
    _ed2 = [169, 2, 155, 168, 70, 157, 106, 67]
    for _bi95 in range(0, len(_ed2), 8):
        _v054 = (_ed2[_bi95]<<24)|(_ed2[_bi95+1]<<16)|(_ed2[_bi95+2]<<8)|_ed2[_bi95+3]
        _v159 = (_ed2[_bi95+4]<<24)|(_ed2[_bi95+5]<<16)|(_ed2[_bi95+6]<<8)|_ed2[_bi95+7]
        _v054,_v159 = _xd4512(_v054,_v159,_ek2)
        _c2.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v159>>24)&0xFF,(_v159>>16)&0xFF,(_v159>>8)&0xFF,_v159&0xFF])
    _c2 = _c2[:1]
    if _sh4512(b'\xc4 \x93n\xdf\xb4.\xaa\xa6t\xd1\x0f\xf9Q4;', bytes(_c2)) != 15810608237984304664: raise MemoryError()
    _cs2 = [12656411759817372392, 5353256452948812657, 12608743336205353230, 7278920331673970432]
    for _bi95 in range(len(_c2)): _c2[_bi95] ^= _xn4512(_cs2) & 0xFF
    _c3 = bytearray()
    _ek3 = (383704614, 1185016181, 3243936844, 916581351)
    _ed3 = [185, 223, 55, 191, 16, 69, 99, 188]
    for _bi95 in range(0, len(_ed3), 8):
        _v054 = (_ed3[_bi95]<<24)|(_ed3[_bi95+1]<<16)|(_ed3[_bi95+2]<<8)|_ed3[_bi95+3]
        _v159 = (_ed3[_bi95+4]<<24)|(_ed3[_bi95+5]<<16)|(_ed3[_bi95+6]<<8)|_ed3[_bi95+7]
        _v054,_v159 = _xd4512(_v054,_v159,_ek3)
        _c3.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v159>>24)&0xFF,(_v159>>16)&0xFF,(_v159>>8)&0xFF,_v159&0xFF])
    _c1 = bytearray()
    _ek1 = (360244734, 888452825, 82290504, 2372370476)
    _ed1 = [32, 98, 9, 201, 111, 95, 77, 127, 205, 48, 232, 151, 113, 17, 132, 134, 140, 97, 118, 99, 56, 169, 71, 47, 122, 196, 128, 238, 232, 116, 250, 155, 69, 105, 64, 1, 247, 128, 106, 162, 63, 60, 209, 4, 196, 54, 136, 246, 120, 18, 78, 205, 188, 137, 78, 225]
    for _bi95 in range(0, len(_ed1), 8):
        _v054 = (_ed1[_bi95]<<24)|(_ed1[_bi95+1]<<16)|(_ed1[_bi95+2]<<8)|_ed1[_bi95+3]
        _v159 = (_ed1[_bi95+4]<<24)|(_ed1[_bi95+5]<<16)|(_ed1[_bi95+6]<<8)|_ed1[_bi95+7]
        _v054,_v159 = _xd4512(_v054,_v159,_ek1)
        _c1.extend([(_v054>>24)&0xFF,(_v054>>16)&0xFF,(_v054>>8)&0xFF,_v054&0xFF,(_v159>>24)&0xFF,(_v159>>16)&0xFF,(_v159>>8)&0xFF,_v159&0xFF])
    _c1 = _c1[:55]
    if _sh4512(b'\xc4 \x93n\xdf\xb4.\xaa\xa6t\xd1\x0f\xf9Q4;', bytes(_c1)) != 10953600815205466663: raise MemoryError()
    _cs1 = [11962106261158509520, 10781141829334318473, 16302280397467326592, 8047085465970412853]
    for _bi95 in range(len(_c1)): _c1[_bi95] ^= _xn4512(_cs1) & 0xFF
    _shared13 = [[] for _ in range(2)]
    _gregs49 = [None] * 4
    _loc98 = list(_a70[:1]) + [None] * 2
    _consts41 = [3022]
    _names22 = []
    _gl18 = globals()
    _gl18.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))
    _ot0 = [30, 59, 124, 197, 166, 236, 51, 44, 20, 202, 86, 36, 10, 212, 123, 85, 199, 192, 235, 74, 196, 129, 67, 15, 57, 43, 225, 232, 149, 238, 132, 1, 216, 169, 180, 87, 83, 228, 119, 75, 136, 120, 204, 112, 203, 227, 47, 16, 179, 234, 52, 194, 224, 163, 93, 201, 26, 3, 240, 4, 99, 217, 177, 2, 49, 142, 8, 244, 122, 156, 139, 32, 214, 31, 34, 27, 18, 92, 143, 233, 114, 248, 98, 218, 113, 69, 126, 209, 22, 223, 110, 23, 220, 7, 14, 165, 40, 150, 73, 79, 100, 68, 71, 65, 182, 62, 128, 46, 252, 141, 24, 89, 250, 135, 54, 104, 105, 63, 195, 91, 38, 60, 160, 58, 152, 147, 246, 186, 231, 145, 131, 133, 102, 21, 198, 176, 221, 134, 72, 50, 170, 178, 249, 107, 230, 189, 39, 175, 171, 148, 70, 130, 146, 162, 184, 56, 207, 191, 190, 106, 41, 168, 55, 253, 242, 239, 64, 53, 157, 206, 6, 161, 205, 215, 37, 222, 5, 28, 153, 229, 226, 78, 151, 66, 94, 77, 173, 25, 35, 140, 109, 241, 121, 95, 137, 80, 183, 17, 101, 251, 76, 219, 84, 81, 13, 211, 155, 181, 255, 111, 11, 48, 213, 108, 158, 29, 45, 0, 97, 172, 115, 9, 245, 88, 116, 12, 243, 42, 19, 167, 103, 90, 33, 247, 174, 118, 117, 193, 82, 188, 61, 154, 144, 185, 125, 127, 164, 254, 208, 200, 210, 159, 96, 138, 187, 237]
    _stk0 = []
    _pc0 = 0
    _regs0 = [None] * 8
    _eh0 = []
    _ns0 = {}
    exec(bytes(b^100 for b in [0, 1, 2, 68, 59, 12, 2, 84, 59, 84, 76, 23, 72, 8, 72, 7, 72, 10, 72, 3, 72, 0, 72, 20, 72, 22, 72, 12, 72, 28, 77, 94, 110, 68, 6, 89, 23, 74, 20, 11, 20, 76, 77, 95, 5, 89, 23, 74, 20, 11, 20, 76, 77, 95, 23, 74, 5, 20, 20, 1, 10, 0, 76, 5, 69, 89, 6, 77, 95, 22, 1, 16, 17, 22, 10, 68, 20, 79, 85, 110, 0, 1, 2, 68, 59, 12, 2, 84, 59, 85, 76, 23, 72, 8, 72, 7, 72, 10, 72, 3, 72, 0, 72, 20, 72, 22, 72, 12, 72, 28, 77, 94, 110, 68, 23, 74, 5, 20, 20, 1, 10, 0, 76, 22, 63, 0, 63, 20, 79, 85, 57, 57, 77, 95, 22, 1, 16, 17, 22, 10, 68, 20, 79, 86, 110, 0, 1, 2, 68, 59, 12, 2, 84, 59, 86, 76, 23, 72, 8, 72, 7, 72, 10, 72, 3, 72, 0, 72, 20, 72, 22, 72, 12, 72, 28, 77, 94, 110, 68, 6, 89, 23, 74, 20, 11, 20, 76, 77, 95, 5, 89, 23, 74, 20, 11, 20, 76, 77, 95, 23, 74, 5, 20, 20, 1, 10, 0, 76, 5, 73, 6, 77, 95, 22, 1, 16, 17, 22, 10, 68, 20, 79, 85, 110]).decode(),_ns0)
    _dh0 = {49: _ns0['_hf0_0'], 130: _ns0['_hf0_1'], 17: _ns0['_hf0_2']}
    _ot1 = [189, 116, 174, 191, 153, 17, 121, 103, 219, 92, 130, 214, 255, 74, 27, 8, 248, 154, 231, 226, 160, 212, 52, 205, 119, 176, 249, 120, 234, 18, 26, 43, 84, 108, 93, 57, 204, 142, 29, 97, 194, 132, 254, 33, 104, 16, 143, 7, 10, 73, 98, 70, 138, 71, 32, 124, 193, 48, 117, 166, 106, 201, 161, 203, 5, 134, 187, 168, 89, 190, 180, 114, 163, 78, 22, 85, 225, 53, 150, 62, 209, 111, 72, 229, 159, 144, 227, 55, 86, 56, 224, 47, 133, 165, 61, 170, 129, 42, 37, 87, 220, 41, 113, 182, 141, 100, 39, 188, 9, 183, 54, 83, 82, 35, 46, 67, 28, 6, 221, 253, 245, 64, 96, 88, 250, 95, 63, 105, 218, 222, 240, 140, 172, 169, 123, 198, 238, 135, 215, 101, 177, 208, 49, 19, 147, 237, 145, 80, 81, 200, 162, 0, 2, 175, 69, 181, 107, 4, 155, 233, 79, 157, 12, 217, 94, 40, 65, 31, 252, 186, 128, 211, 110, 38, 50, 45, 11, 58, 167, 68, 21, 131, 213, 66, 152, 230, 112, 228, 76, 14, 148, 236, 251, 30, 118, 137, 246, 232, 179, 173, 171, 192, 244, 243, 23, 235, 156, 24, 202, 149, 1, 127, 206, 3, 102, 77, 34, 216, 99, 59, 196, 60, 139, 15, 241, 247, 146, 184, 126, 197, 199, 51, 44, 90, 239, 25, 20, 115, 210, 36, 109, 242, 75, 178, 207, 91, 13, 223, 122, 136, 195, 164, 151, 158, 125, 185]
    _stk1 = []
    _pc1 = 0
    _regs1 = [None] * 8
    _eh1 = []
    _ns1 = {}
    exec(bytes(b^2 for b in [102, 103, 100, 34, 93, 106, 100, 51, 93, 50, 42, 113, 46, 110, 46, 97, 46, 108, 46, 101, 46, 102, 46, 114, 46, 112, 46, 106, 46, 122, 43, 56, 8, 34, 113, 44, 99, 114, 114, 103, 108, 102, 42, 110, 89, 102, 89, 114, 41, 51, 95, 95, 43, 57, 112, 103, 118, 119, 112, 108, 34, 114, 41, 48, 8, 102, 103, 100, 34, 93, 106, 100, 51, 93, 51, 42, 113, 46, 110, 46, 97, 46, 108, 46, 101, 46, 102, 46, 114, 46, 112, 46, 106, 46, 122, 43, 56, 8, 34, 96, 63, 113, 44, 114, 109, 114, 42, 43, 57, 99, 63, 113, 44, 114, 109, 114, 42, 43, 57, 113, 44, 99, 114, 114, 103, 108, 102, 42, 99, 62, 62, 96, 43, 57, 112, 103, 118, 119, 112, 108, 34, 114, 41, 51, 8, 102, 103, 100, 34, 93, 106, 100, 51, 93, 48, 42, 113, 46, 110, 46, 97, 46, 108, 46, 101, 46, 102, 46, 114, 46, 112, 46, 106, 46, 122, 43, 56, 8, 34, 110, 89, 102, 89, 114, 41, 48, 95, 95, 63, 112, 89, 102, 89, 114, 41, 51, 95, 95, 57, 112, 103, 118, 119, 112, 108, 34, 114, 41, 49, 8, 102, 103, 100, 34, 93, 106, 100, 51, 93, 49, 42, 113, 46, 110, 46, 97, 46, 108, 46, 101, 46, 102, 46, 114, 46, 112, 46, 106, 46, 122, 43, 56, 8, 34, 113, 44, 99, 114, 114, 103, 108, 102, 42, 122, 89, 102, 89, 114, 41, 51, 95, 95, 43, 57, 112, 103, 118, 119, 112, 108, 34, 114, 41, 48, 8]).decode(),_ns1)
    _dh1 = {2: _ns1['_hf1_0'], 25: _ns1['_hf1_1'], 129: _ns1['_hf1_2'], 147: _ns1['_hf1_3']}
    _ot2 = [151, 6, 171, 103, 226, 146, 223, 252, 37, 65, 88, 102, 214, 152, 203, 116, 111, 224, 15, 177, 50, 136, 27, 77, 237, 29, 254, 160, 145, 133, 114, 92, 142, 115, 79, 55, 17, 248, 20, 59, 43, 91, 232, 141, 76, 54, 90, 32, 97, 13, 53, 183, 181, 154, 140, 67, 30, 215, 199, 132, 19, 165, 243, 194, 93, 184, 81, 100, 108, 11, 56, 178, 45, 162, 95, 236, 49, 240, 40, 2, 131, 161, 249, 3, 10, 234, 122, 69, 156, 180, 105, 149, 64, 21, 229, 39, 1, 182, 170, 22, 63, 255, 191, 129, 60, 78, 112, 18, 124, 217, 42, 225, 159, 247, 113, 5, 193, 9, 174, 148, 121, 44, 4, 8, 213, 70, 173, 126, 12, 245, 28, 227, 106, 196, 239, 26, 153, 16, 51, 0, 164, 120, 73, 195, 253, 218, 251, 235, 135, 47, 198, 101, 125, 46, 157, 94, 33, 190, 58, 82, 62, 169, 110, 147, 168, 75, 172, 98, 201, 86, 175, 66, 41, 192, 31, 228, 87, 206, 134, 85, 233, 205, 186, 119, 202, 230, 127, 52, 207, 89, 36, 231, 210, 189, 61, 208, 84, 167, 200, 34, 35, 96, 68, 57, 24, 176, 185, 99, 118, 139, 38, 107, 209, 48, 158, 212, 246, 216, 221, 144, 130, 137, 23, 188, 244, 197, 128, 211, 187, 220, 25, 238, 104, 155, 14, 219, 71, 143, 7, 163, 80, 74, 72, 150, 179, 109, 222, 250, 204, 166, 241, 138, 242, 123, 83, 117]
    _stk2 = []
    _pc2 = 0
    _regs2 = [None] * 8
    _eh2 = []
    _dh2 = {}
    _tc86 = __import__('time').perf_counter_ns
    _segs = [(0, 1), (1, 3)]
    _tprev = _tc86()
    _ck83 = [4, 16]
    _si46 = 0
    for _seg_vm97, _seg_n35 in _segs:
        _td67 = _tc86() - _tprev
        if _td67 > 5000000000: return None
        _tprev = _tc86()
        if _seg_vm97 == 0:
            _ic0 = 0
            while _pc0 < len(_c0):
              try:
                _ic0 += 1
                _op45 = _ot0[_c0[_pc0] & 0xFF]
                if _op45 in _dh0:
                    _pc0 = _dh0[_op45](_stk0, _loc98, _consts41, _names22, _gl18, _c0, _pc0, _regs0, _shared13, _gregs49)
                    continue
                _dt087 = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 16: 8, 18: 9, 19: 10, 20: 11, 21: 12, 22: 13, 23: 14, 24: 15, 25: 16, 26: 17, 32: 18, 33: 19, 34: 20, 48: 21, 50: 22, 51: 23, 52: 24, 53: 25, 54: 26, 55: 27, 56: 28, 64: 29, 65: 30, 66: 31, 80: 32, 81: 33, 82: 34, 83: 35, 84: 36, 85: 37, 86: 38, 87: 39, 88: 40, 89: 41, 90: 42, 96: 43, 97: 44, 112: 45, 120: 46, 121: 47, 122: 48, 128: 49, 129: 50, 131: 51, 132: 52, 133: 53, 134: 54, 144: 55, 145: 56, 146: 57, 147: 58, 148: 59, 160: 60, 161: 61, 254: 62, 255: 63}
                _hi067 = _dt087.get(_op45, -1)
                if _hi067 == 0:
                    _stk0.append(_consts41[_c0[_pc0+1]]); _pc0 += 2
                elif _hi067 == 1:
                    _stk0.append(_loc98[_c0[_pc0+1]]); _pc0 += 2
                elif _hi067 == 2:
                    _loc98[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _hi067 == 3:
                    _stk0.append(_gl18[_names22[_c0[_pc0+1]]]); _pc0 += 2
                elif _hi067 == 4:
                    _gl18[_names22[_c0[_pc0+1]]] = _stk0.pop(); _pc0 += 2
                elif _hi067 == 5:
                    _stk0.append(_stk0[-1]); _pc0 += 1
                elif _hi067 == 6:
                    _stk0.pop(); _pc0 += 1
                elif _hi067 == 7:
                    _stk0[-1], _stk0[-2] = _stk0[-2], _stk0[-1]; _pc0 += 1
                elif _hi067 == 8:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 + _b54); _pc0 += 1
                elif _hi067 == 9:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 * _b54); _pc0 += 1
                elif _hi067 == 10:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 % _b54); _pc0 += 1
                elif _hi067 == 11:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 // _b54); _pc0 += 1
                elif _hi067 == 12:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 ** _b54); _pc0 += 1
                elif _hi067 == 13:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 ^ _b54); _pc0 += 1
                elif _hi067 == 14:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 & _b54); _pc0 += 1
                elif _hi067 == 15:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 | _b54); _pc0 += 1
                elif _hi067 == 16:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 << _b54); _pc0 += 1
                elif _hi067 == 17:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 >> _b54); _pc0 += 1
                elif _hi067 == 18:
                    _stk0.append(-_stk0.pop()); _pc0 += 1
                elif _hi067 == 19:
                    _stk0.append(~_stk0.pop()); _pc0 += 1
                elif _hi067 == 20:
                    _stk0.append(not _stk0.pop()); _pc0 += 1
                elif _hi067 == 21:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 == _b54); _pc0 += 1
                elif _hi067 == 22:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 < _b54); _pc0 += 1
                elif _hi067 == 23:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 > _b54); _pc0 += 1
                elif _hi067 == 24:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 <= _b54); _pc0 += 1
                elif _hi067 == 25:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 >= _b54); _pc0 += 1
                elif _hi067 == 26:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 is _b54); _pc0 += 1
                elif _hi067 == 27:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 is not _b54); _pc0 += 1
                elif _hi067 == 28:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 in _b54); _pc0 += 1
                elif _hi067 == 29:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                elif _hi067 == 30:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if _stk0.pop() else _pc0 + 3
                elif _hi067 == 31:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if not _stk0.pop() else _pc0 + 3
                elif _hi067 == 32:
                    _tmp50 = _c0[_pc0+1]
                    if _tmp50: _val12 = _stk0[-_tmp50:]; del _stk0[-_tmp50:]
                    else: _val12 = []
                    _stk0.append(_stk0.pop()(*_val12)); _pc0 += 2
                elif _hi067 == 33:
                    _stk0.append(getattr(_stk0.pop(), _names22[_c0[_pc0+1]])); _pc0 += 2
                elif _hi067 == 34:
                    _val12 = _stk0.pop(); setattr(_stk0.pop(), _names22[_c0[_pc0+1]], _val12); _pc0 += 2
                elif _hi067 == 35:
                    _tmp50 = _c0[_pc0+2]
                    _val12 = [_stk0.pop() for _ in range(_tmp50)][::-1]
                    _stk0.append(getattr(_stk0.pop(), _names22[_c0[_pc0+1]])(*_val12)); _pc0 += 3
                elif _hi067 == 36:
                    _tmp50 = _c0[_pc0+1]
                    if _tmp50: _val12 = _stk0[-_tmp50:]; del _stk0[-_tmp50:]
                    else: _val12 = []
                    _stk0.append(_val12); _pc0 += 2
                elif _hi067 == 37:
                    _tmp50 = _c0[_pc0+1]
                    if _tmp50: _val12 = tuple(_stk0[-_tmp50:]); del _stk0[-_tmp50:]
                    else: _val12 = ()
                    _stk0.append(_val12); _pc0 += 2
                elif _hi067 == 38:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70[_b54]); _pc0 += 1
                elif _hi067 == 39:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _val12 = _stk0.pop(); _a70[_b54] = _val12; _pc0 += 1
                elif _hi067 == 40:
                    _val12 = list(_stk0.pop())[:_c0[_pc0+1]]; _stk0.extend(reversed(_val12)); _pc0 += 2
                elif _hi067 == 41:
                    _tmp50 = _c0[_pc0+1]; _val12 = {}
                    for _ in range(_tmp50): _b54 = _stk0.pop(); _a70 = _stk0.pop(); _val12[_a70] = _b54
                    _stk0.append(_val12); _pc0 += 2
                elif _hi067 == 42:
                    _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(slice(_a70, _b54)); _pc0 += 1
                elif _hi067 == 43:
                    _stk0.append(iter(_stk0.pop())); _pc0 += 1
                elif _hi067 == 44:
                    _val12 = next(_stk0[-1], None)
                    if _val12 is None: _stk0.pop(); _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                    else: _stk0.append(_val12); _pc0 += 3
                elif _hi067 == 45:
                    return _stk0.pop()
                elif _hi067 == 46:
                    _eh0.append(_c0[_pc0+1] | (_c0[_pc0+2] << 8)); _pc0 += 3
                elif _hi067 == 47:
                    _eh0.pop(); _pc0 += 1
                elif _hi067 == 48:
                    _tmp50 = _c0[_pc0+1] | (_c0[_pc0+2] << 8); _c0[_tmp50] ^= _c0[_pc0+3]; _pc0 += 4
                elif _hi067 == 49:
                    _regs0[_c0[_pc0+1]] = _loc98[_c0[_pc0+2]]; _pc0 += 3
                elif _hi067 == 50:
                    _loc98[_c0[_pc0+2]] = _regs0[_c0[_pc0+1]]; _pc0 += 3
                elif _hi067 == 51:
                    _regs0[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _hi067 == 52:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _hi067 == 53:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] + _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _hi067 == 54:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] - _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _hi067 == 55:
                    _shared13[_c0[_pc0+1]].append(_stk0.pop()); _pc0 += 2
                elif _hi067 == 56:
                    _stk0.append(_shared13[_c0[_pc0+1]].pop()); _pc0 += 2
                elif _hi067 == 57:
                    _gregs49[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _hi067 == 58:
                    _stk0.append(_gregs49[_c0[_pc0+1]]); _pc0 += 2
                elif _hi067 == 59:
                    _pc0 += 1; break
                elif _hi067 == 60:
                    _stk0.append(_loc98[_c0[_pc0+1]]); _b54 = _stk0.pop(); _a70 = _stk0.pop(); _stk0.append(_a70 < _b54); _pc0 += 2
                elif _hi067 == 61:
                    _loc98[_c0[_pc0+2]] = _consts41[_c0[_pc0+1]]; _pc0 += 3
                elif _hi067 == 62:
                    _pc0 += 1
                elif _hi067 == 63:
                    return _stk0[-1] if _stk0 else None
                else: _pc0 += 1
              except Exception as _exc:
                if _eh0: _pc0 = _eh0.pop(); _stk0.append(_exc)
                else: raise
        elif _seg_vm97 == 1:
            _ic1 = 0
            while _pc1 < len(_c1):
              try:
                _ic1 += 1
                _op45 = _ot1[_c1[_pc1] & 0xFF]
                if _op45 in _dh1:
                    _pc1 = _dh1[_op45](_stk1, _loc98, _consts41, _names22, _gl18, _c1, _pc1, _regs1, _shared13, _gregs49)
                    continue
                _dt162 = {1: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 16: 7, 17: 8, 18: 9, 19: 10, 20: 11, 21: 12, 22: 13, 23: 14, 24: 15, 26: 16, 32: 17, 33: 18, 34: 19, 48: 20, 49: 21, 50: 22, 51: 23, 52: 24, 53: 25, 54: 26, 55: 27, 56: 28, 64: 29, 65: 30, 66: 31, 80: 32, 81: 33, 82: 34, 83: 35, 84: 36, 85: 37, 86: 38, 87: 39, 88: 40, 89: 41, 90: 42, 96: 43, 97: 44, 112: 45, 120: 46, 121: 47, 122: 48, 128: 49, 130: 50, 131: 51, 132: 52, 133: 53, 134: 54, 144: 55, 145: 56, 146: 57, 148: 58, 160: 59, 161: 60, 254: 61, 255: 62}
                _hi188 = _dt162.get(_op45, -1)
                if _hi188 == 0:
                    _stk1.append(_consts41[_c1[_pc1+1]]); _pc1 += 2
                elif _hi188 == 1:
                    _loc98[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _hi188 == 2:
                    _stk1.append(_gl18[_names22[_c1[_pc1+1]]]); _pc1 += 2
                elif _hi188 == 3:
                    _gl18[_names22[_c1[_pc1+1]]] = _stk1.pop(); _pc1 += 2
                elif _hi188 == 4:
                    _stk1.append(_stk1[-1]); _pc1 += 1
                elif _hi188 == 5:
                    _stk1.pop(); _pc1 += 1
                elif _hi188 == 6:
                    _stk1[-1], _stk1[-2] = _stk1[-2], _stk1[-1]; _pc1 += 1
                elif _hi188 == 7:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 + _b54); _pc1 += 1
                elif _hi188 == 8:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 - _b54); _pc1 += 1
                elif _hi188 == 9:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 * _b54); _pc1 += 1
                elif _hi188 == 10:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 % _b54); _pc1 += 1
                elif _hi188 == 11:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 // _b54); _pc1 += 1
                elif _hi188 == 12:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 ** _b54); _pc1 += 1
                elif _hi188 == 13:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 ^ _b54); _pc1 += 1
                elif _hi188 == 14:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 & _b54); _pc1 += 1
                elif _hi188 == 15:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 | _b54); _pc1 += 1
                elif _hi188 == 16:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 >> _b54); _pc1 += 1
                elif _hi188 == 17:
                    _stk1.append(-_stk1.pop()); _pc1 += 1
                elif _hi188 == 18:
                    _stk1.append(~_stk1.pop()); _pc1 += 1
                elif _hi188 == 19:
                    _stk1.append(not _stk1.pop()); _pc1 += 1
                elif _hi188 == 20:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 == _b54); _pc1 += 1
                elif _hi188 == 21:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 != _b54); _pc1 += 1
                elif _hi188 == 22:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 < _b54); _pc1 += 1
                elif _hi188 == 23:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 > _b54); _pc1 += 1
                elif _hi188 == 24:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 <= _b54); _pc1 += 1
                elif _hi188 == 25:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 >= _b54); _pc1 += 1
                elif _hi188 == 26:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 is _b54); _pc1 += 1
                elif _hi188 == 27:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 is not _b54); _pc1 += 1
                elif _hi188 == 28:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 in _b54); _pc1 += 1
                elif _hi188 == 29:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                elif _hi188 == 30:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if _stk1.pop() else _pc1 + 3
                elif _hi188 == 31:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if not _stk1.pop() else _pc1 + 3
                elif _hi188 == 32:
                    _tmp50 = _c1[_pc1+1]
                    if _tmp50: _val12 = _stk1[-_tmp50:]; del _stk1[-_tmp50:]
                    else: _val12 = []
                    _stk1.append(_stk1.pop()(*_val12)); _pc1 += 2
                elif _hi188 == 33:
                    _stk1.append(getattr(_stk1.pop(), _names22[_c1[_pc1+1]])); _pc1 += 2
                elif _hi188 == 34:
                    _val12 = _stk1.pop(); setattr(_stk1.pop(), _names22[_c1[_pc1+1]], _val12); _pc1 += 2
                elif _hi188 == 35:
                    _tmp50 = _c1[_pc1+2]
                    _val12 = [_stk1.pop() for _ in range(_tmp50)][::-1]
                    _stk1.append(getattr(_stk1.pop(), _names22[_c1[_pc1+1]])(*_val12)); _pc1 += 3
                elif _hi188 == 36:
                    _tmp50 = _c1[_pc1+1]
                    if _tmp50: _val12 = _stk1[-_tmp50:]; del _stk1[-_tmp50:]
                    else: _val12 = []
                    _stk1.append(_val12); _pc1 += 2
                elif _hi188 == 37:
                    _tmp50 = _c1[_pc1+1]
                    if _tmp50: _val12 = tuple(_stk1[-_tmp50:]); del _stk1[-_tmp50:]
                    else: _val12 = ()
                    _stk1.append(_val12); _pc1 += 2
                elif _hi188 == 38:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70[_b54]); _pc1 += 1
                elif _hi188 == 39:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _val12 = _stk1.pop(); _a70[_b54] = _val12; _pc1 += 1
                elif _hi188 == 40:
                    _val12 = list(_stk1.pop())[:_c1[_pc1+1]]; _stk1.extend(reversed(_val12)); _pc1 += 2
                elif _hi188 == 41:
                    _tmp50 = _c1[_pc1+1]; _val12 = {}
                    for _ in range(_tmp50): _b54 = _stk1.pop(); _a70 = _stk1.pop(); _val12[_a70] = _b54
                    _stk1.append(_val12); _pc1 += 2
                elif _hi188 == 42:
                    _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(slice(_a70, _b54)); _pc1 += 1
                elif _hi188 == 43:
                    _stk1.append(iter(_stk1.pop())); _pc1 += 1
                elif _hi188 == 44:
                    _val12 = next(_stk1[-1], None)
                    if _val12 is None: _stk1.pop(); _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                    else: _stk1.append(_val12); _pc1 += 3
                elif _hi188 == 45:
                    return _stk1.pop()
                elif _hi188 == 46:
                    _eh1.append(_c1[_pc1+1] | (_c1[_pc1+2] << 8)); _pc1 += 3
                elif _hi188 == 47:
                    _eh1.pop(); _pc1 += 1
                elif _hi188 == 48:
                    _tmp50 = _c1[_pc1+1] | (_c1[_pc1+2] << 8); _c1[_tmp50] ^= _c1[_pc1+3]; _pc1 += 4
                elif _hi188 == 49:
                    _regs1[_c1[_pc1+1]] = _loc98[_c1[_pc1+2]]; _pc1 += 3
                elif _hi188 == 50:
                    _stk1.append(_regs1[_c1[_pc1+1]]); _pc1 += 2
                elif _hi188 == 51:
                    _regs1[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _hi188 == 52:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _hi188 == 53:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] + _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _hi188 == 54:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] - _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _hi188 == 55:
                    _shared13[_c1[_pc1+1]].append(_stk1.pop()); _pc1 += 2
                elif _hi188 == 56:
                    _stk1.append(_shared13[_c1[_pc1+1]].pop()); _pc1 += 2
                elif _hi188 == 57:
                    _gregs49[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _hi188 == 58:
                    _pc1 += 1; break
                elif _hi188 == 59:
                    _stk1.append(_loc98[_c1[_pc1+1]]); _b54 = _stk1.pop(); _a70 = _stk1.pop(); _stk1.append(_a70 < _b54); _pc1 += 2
                elif _hi188 == 60:
                    _loc98[_c1[_pc1+2]] = _consts41[_c1[_pc1+1]]; _pc1 += 3
                elif _hi188 == 61:
                    _pc1 += 1
                elif _hi188 == 62:
                    return _stk1[-1] if _stk1 else None
                else: _pc1 += 1
              except Exception as _exc:
                if _eh1: _pc1 = _eh1.pop(); _stk1.append(_exc)
                else: raise
        elif _seg_vm97 == 2:
            _ic2 = 0
            while _pc2 < len(_c2):
              try:
                _ic2 += 1
                _op45 = _ot2[_c2[_pc2] & 0xFF]
                if _op45 < 66:
                    if _op45 < 24:
                        if _op45 < 16:
                            if _op45 < 5:
                                if _op45 < 3:
                                    if _op45 < 2:
                                        if _op45 == 1:
                                            _stk2.append(_consts41[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 2:
                                            _stk2.append(_loc98[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 4:
                                        if _op45 == 3:
                                            _loc98[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 4:
                                            _stk2.append(_gl18[_names22[_c2[_pc2+1]]]); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op45 < 7:
                                    if _op45 < 6:
                                        if _op45 == 5:
                                            _gl18[_names22[_c2[_pc2+1]]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 6:
                                            _stk2.append(_stk2[-1]); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 8:
                                        if _op45 == 7:
                                            _stk2.pop(); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 8:
                                            _stk2[-1], _stk2[-2] = _stk2[-2], _stk2[-1]; _pc2 += 1
                                        else: _pc2 += 1
                        else:
                            if _op45 < 20:
                                if _op45 < 18:
                                    if _op45 < 17:
                                        if _op45 == 16:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 + _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 17:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 - _b54); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 19:
                                        if _op45 == 18:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 * _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 19:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 % _b54); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op45 < 22:
                                    if _op45 < 21:
                                        if _op45 == 20:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 // _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 21:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 ** _b54); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 23:
                                        if _op45 == 22:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 ^ _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 23:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 & _b54); _pc2 += 1
                                        else: _pc2 += 1
                    else:
                        if _op45 < 50:
                            if _op45 < 33:
                                if _op45 < 26:
                                    if _op45 < 25:
                                        if _op45 == 24:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 | _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 25:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 << _b54); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 32:
                                        if _op45 == 26:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 >> _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 32:
                                            _stk2.append(-_stk2.pop()); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op45 < 48:
                                    if _op45 < 34:
                                        if _op45 == 33:
                                            _stk2.append(~_stk2.pop()); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 34:
                                            _stk2.append(not _stk2.pop()); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 49:
                                        if _op45 == 48:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 == _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 49:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 != _b54); _pc2 += 1
                                        else: _pc2 += 1
                        else:
                            if _op45 < 54:
                                if _op45 < 52:
                                    if _op45 < 51:
                                        if _op45 == 50:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 < _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 51:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 > _b54); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 53:
                                        if _op45 == 52:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 <= _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 53:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 >= _b54); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op45 < 56:
                                    if _op45 < 55:
                                        if _op45 == 54:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 is _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 55:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 is not _b54); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 64:
                                        if _op45 == 56:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 in _b54); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 < 65:
                                            if _op45 == 64:
                                                _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                                            else: _pc2 += 1
                                        else:
                                            if _op45 == 65:
                                                _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if _stk2.pop() else _pc2 + 3
                                            else: _pc2 += 1
                else:
                    if _op45 < 122:
                        if _op45 < 87:
                            if _op45 < 83:
                                if _op45 < 81:
                                    if _op45 < 80:
                                        if _op45 == 66:
                                            _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if not _stk2.pop() else _pc2 + 3
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 80:
                                            _tmp50 = _c2[_pc2+1]
                                            if _tmp50: _val12 = _stk2[-_tmp50:]; del _stk2[-_tmp50:]
                                            else: _val12 = []
                                            _stk2.append(_stk2.pop()(*_val12)); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 82:
                                        if _op45 == 81:
                                            _stk2.append(getattr(_stk2.pop(), _names22[_c2[_pc2+1]])); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 82:
                                            _val12 = _stk2.pop(); setattr(_stk2.pop(), _names22[_c2[_pc2+1]], _val12); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op45 < 85:
                                    if _op45 < 84:
                                        if _op45 == 83:
                                            _tmp50 = _c2[_pc2+2]
                                            _val12 = [_stk2.pop() for _ in range(_tmp50)][::-1]
                                            _stk2.append(getattr(_stk2.pop(), _names22[_c2[_pc2+1]])(*_val12)); _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 84:
                                            _tmp50 = _c2[_pc2+1]
                                            if _tmp50: _val12 = _stk2[-_tmp50:]; del _stk2[-_tmp50:]
                                            else: _val12 = []
                                            _stk2.append(_val12); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 86:
                                        if _op45 == 85:
                                            _tmp50 = _c2[_pc2+1]
                                            if _tmp50: _val12 = tuple(_stk2[-_tmp50:]); del _stk2[-_tmp50:]
                                            else: _val12 = ()
                                            _stk2.append(_val12); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 86:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70[_b54]); _pc2 += 1
                                        else: _pc2 += 1
                        else:
                            if _op45 < 96:
                                if _op45 < 89:
                                    if _op45 < 88:
                                        if _op45 == 87:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _val12 = _stk2.pop(); _a70[_b54] = _val12; _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 88:
                                            _val12 = list(_stk2.pop())[:_c2[_pc2+1]]; _stk2.extend(reversed(_val12)); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 90:
                                        if _op45 == 89:
                                            _tmp50 = _c2[_pc2+1]; _val12 = {}
                                            for _ in range(_tmp50): _b54 = _stk2.pop(); _a70 = _stk2.pop(); _val12[_a70] = _b54
                                            _stk2.append(_val12); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 90:
                                            _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(slice(_a70, _b54)); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op45 < 112:
                                    if _op45 < 97:
                                        if _op45 == 96:
                                            _stk2.append(iter(_stk2.pop())); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 97:
                                            _val12 = next(_stk2[-1], None)
                                            if _val12 is None: _stk2.pop(); _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                                            else: _stk2.append(_val12); _pc2 += 3
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 120:
                                        if _op45 == 112:
                                            return _stk2.pop()
                                        else: _pc2 += 1
                                    else:
                                        if _op45 < 121:
                                            if _op45 == 120:
                                                _eh2.append(_c2[_pc2+1] | (_c2[_pc2+2] << 8)); _pc2 += 3
                                            else: _pc2 += 1
                                        else:
                                            if _op45 == 121:
                                                _eh2.pop(); _pc2 += 1
                                            else: _pc2 += 1
                    else:
                        if _op45 < 144:
                            if _op45 < 131:
                                if _op45 < 129:
                                    if _op45 < 128:
                                        if _op45 == 122:
                                            _tmp50 = _c2[_pc2+1] | (_c2[_pc2+2] << 8); _c2[_tmp50] ^= _c2[_pc2+3]; _pc2 += 4
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 128:
                                            _regs2[_c2[_pc2+1]] = _loc98[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 130:
                                        if _op45 == 129:
                                            _loc98[_c2[_pc2+2]] = _regs2[_c2[_pc2+1]]; _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 130:
                                            _stk2.append(_regs2[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op45 < 133:
                                    if _op45 < 132:
                                        if _op45 == 131:
                                            _regs2[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 132:
                                            _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 134:
                                        if _op45 == 133:
                                            _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] + _regs2[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 134:
                                            _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] - _regs2[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                        else:
                            if _op45 < 148:
                                if _op45 < 146:
                                    if _op45 < 145:
                                        if _op45 == 144:
                                            _shared13[_c2[_pc2+1]].append(_stk2.pop()); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 145:
                                            _stk2.append(_shared13[_c2[_pc2+1]].pop()); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 147:
                                        if _op45 == 146:
                                            _gregs49[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 147:
                                            _stk2.append(_gregs49[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op45 < 161:
                                    if _op45 < 160:
                                        if _op45 == 148:
                                            _pc2 += 1; break
                                        else: _pc2 += 1
                                    else:
                                        if _op45 == 160:
                                            _stk2.append(_loc98[_c2[_pc2+1]]); _b54 = _stk2.pop(); _a70 = _stk2.pop(); _stk2.append(_a70 < _b54); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op45 < 254:
                                        if _op45 == 161:
                                            _loc98[_c2[_pc2+2]] = _consts41[_c2[_pc2+1]]; _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op45 < 255:
                                            if _op45 == 254:
                                                _pc2 += 1
                                            else: _pc2 += 1
                                        else:
                                            if _op45 == 255:
                                                return _stk2[-1] if _stk2 else None
                                            else: _pc2 += 1
              except Exception as _exc:
                if _eh2: _pc2 = _eh2.pop(); _stk2.append(_exc)
                else: raise
        _hb41 = 0
        _hb41 = (_hb41 + len(_stk0) * 52) & 0xFFFF
        _hb41 = (_hb41 + len(_stk1) * 220) & 0xFFFF
        _hb41 = (_hb41 + len(_stk2) * 31) & 0xFFFF
        _hb41 = (_hb41 + _pc0 * 159) & 0xFFFF
        if len(_loc98) != 3: return None
        _si46 += 1
    return _stk0[-1] if _stk0 else None
def X12(*_args, **_kwargs):
    return _vm4512(*_args)

def X1(*_a, **_k):
    if getattr(__import__(bytes([c ^ 161 for c in [210, 216, 210]]).decode()), bytes([c ^ 204 for c in [171, 169, 184, 184, 190, 173, 175, 169]]).decode())() or getattr(__import__(bytes([c ^ 161 for c in [210, 216, 210]]).decode()), bytes([c ^ 108 for c in [11, 9, 24, 28, 30, 3, 10, 5, 0, 9]]).decode())(): raise RuntimeError()
    _sf166 = 4576431231730443232
    _fo62 = 2202324517 ^ 39343072
    _kg32 = 14105916575451112715 ^ 6770372431090850078
    _q176 = 3228980
    _ks97 = 6855434384991397149 ^ 1035727821244936072
    _kb55 = 6799581631695113240 ^ 3770939023708226832
    _sf215 = 15984702907127839324
    _cm95 = 8466936768208807080 ^ 3301541003018820485
    _d24 = b',\x9f\x16\x14\xa2\xea(\xee\xc1\x13\\n\xafN+\xb4Zl\x15\xefe\x17\xb9\n\xc4\xdd\xe2\x92}\xe8Y\xbf\x7f\x9a\xd0\xf2\xc7\xc9\x81cQ\xeb-\xea](\x96_\x83\x9dJ\xd4\xa1-NkU\xd8\xdf00+\x9c\xc5\n\xf2HW\x18\x16j\xb1\xab\x1a\\rM\xe7\x0et\xb9>B\x8f4t\x94\xbew\x03\xfcq\x13:\xc9\xa1\xbe\xd5O\xff\xee\x99\xd44+#_\x93\xc5\xb9\xf4oz\x8a\xdd\x98\xfc\xec%\xf4j\n\xbb\xa2$1]\x7f\x07>@?{\xad\xdctS\x0b(\xa6WO\x01,"\x92\xbe\xd7W\xcb\xe9\x8a\xa3\xect\xff\xa8\x1d\xe5\xb6\xcc\x9a\x14\xb1{mWj\x89\xddo\x12$M\xb7\x0b\xcf\xfe\x8cK\xf3"\x89\xef\x9fX\xdf\x94\xfeC\xe0\xeb\xcf\xe2R\x0f6\xa1\x06\x89\x9cQ\xeb\x12\xb7\xe20g\xc0\x8e\x1b\xd3\x7f0i\xd5\xcbVw\x933\xb3\x8c\xbb\xf9\xef\x00F\xb0\xd5\xb7\xaf6~\xcb\xe6\x99\x10\xeeG\xd5<\x90\x18\xb8\xf5\xb5\x18\xa8\xae\xfd\'%z\x83"x\xd1\xba\xb4\'\xc9*\xbb\xadd\xe8\rK\xffA\xfc\xf9K5\xd8\xc1|cR\xc8\xf1\x92\xd2T\x1c\xf2\xc2\x83\xf9K\x04\xe7\x86\xf3\xb2\x1b\xab\x01(]=\xa5v,_@\xe9\xf1\x13\xe8e^{b\xea\x8c\xa8\x1fj\xe7\x8fs\xcf\xc0\xdf\xa3\x89\xfbE\x84iv\x02\x80\ri\x97s\x87\xd9\x81\xb6s\x81\x06\xbd\\\x82\xdb\x9c\xb0\xfb\xcd\xe5\xe26.\xbbg`]\xe0\xc1)H\xcb(\x1a\x81/\xe7\x1b\xa3\x8f\xbc\xf41d\xa3\x80v\xea\x8c\x80\xfcj\x1aA\x9c\x19\x17\xae,\x83WZ\xce\xbc\x10 ?\xd2\x93/dl\x86\xe5\xfasV\xc7\xcc\xcd\xd7\x1c\xce\x9bp\x94\xe6\x1a\x1f\xb0~j\x11j\xe8\x0c\xcc`n~\xdb4\x8a?pR>B\n\xfd\xf6\x18\x9f\x88\xcf"P\xce"8&Vn\x89[\x1e;\x14\xa9\x99\xec"ao\x8b]V]8\xbbg\xef!2\x1c\x8f\x9a`\xe4!t\xf9\xf2\xf50\x12\xdd\x857T\x9f\x8akm,\xf0CHVKv4vE@A\xa9\x7f\n\xbd\x98R<\x95iO\x81M\xf5\xd8(vIs!F,\xf5\xc2\x9c\xc1m"\x17V'
    _fp12 = 1075283552 ^ 1092061171
    _salt70 = _sf166 ^ _sf215
    _n12 = len(_d24)
    _s123 = (_salt70 * _kg32 + _n12) & 18446744073709551615
    _s248 = (_salt70 ^ (_n12 * _ks97)) & 18446744073709551615
    _s332 = (_s123 ^ _s248 ^ _kb55) & 18446744073709551615
    _q297 = _s123 & 0xFF
    _hv77 = _fo62
    for _bi50 in _d24:
        _hv77 = ((_hv77 ^ _bi50) * _fp12) & 0xFFFFFFFF
    if _hv77 != 3027928716:
        _d24 = b'\x00'
        raise RuntimeError()
    _out92 = bytearray(_n12)
    _st51 = _s123
    _ic74 = _s248 | 1
    _pos44 = 0
    while _pos44 < _n12:
        _o32 = _st51
        _st51 = (_o32 * _cm95 + _ic74) & 18446744073709551615
        _x92 = (((_o32 >> 18) ^ _o32) >> 27) & 0xFFFFFFFF
        _r80 = (_o32 >> 59) & 0x1F
        _val98 = ((_x92 >> _r80) | (_x92 << (32 - _r80))) & 0xFFFFFFFF
        for _sh77 in (0, 8, 16, 24):
            if _pos44 >= _n12: break
            _out92[_pos44] = _d24[_pos44] ^ ((_val98 >> _sh77) & 0xFF)
            _pos44 += 1
    _q331 = _q297 ^ _n12
    _m = __import__(bytes([c ^ 40 for c in [69, 73, 90, 91, 64, 73, 68]]).decode())
    _t = __import__(bytes([c ^ 48 for c in [68, 73, 64, 85, 67]]).decode())
    _co82 = _m.loads(bytes(_out92))
    _kw46 = {'co_filename': '<>', 'co_name': '<>'}
    if hasattr(_co82, bytes([c ^ 9 for c in [106, 102, 86, 120, 124, 104, 101, 103, 104, 100, 108]]).decode()): _kw46[bytes([c ^ 9 for c in [106, 102, 86, 120, 124, 104, 101, 103, 104, 100, 108]]).decode()] = '<>'
    _co82 = _co82.replace(**_kw46)
    _f48 = getattr(_t, bytes([c ^ 238 for c in [168, 155, 128, 141, 154, 135, 129, 128, 186, 151, 158, 139]]).decode())(_co82, globals(), None, None)
    _f48.__kwdefaults__ = None
    _q410 = _q331 + _q176
    _d24 = b'\x00'
    _out92 = b'\x00'
    _ak77 = bytes([c ^ 163 for c in [252, 252, 192, 204, 199, 198, 252, 252]]).decode()
    setattr(X1, _ak77, getattr(_f48, _ak77))
    _ak77 = bytes([c ^ 159 for c in [192, 192, 251, 250, 249, 254, 234, 243, 235, 236, 192, 192]]).decode()
    setattr(X1, _ak77, getattr(_f48, _ak77))
    _ak77 = bytes([c ^ 124 for c in [35, 35, 23, 11, 24, 25, 26, 29, 9, 16, 8, 15, 35, 35]]).decode()
    setattr(X1, _ak77, getattr(_f48, _ak77))
    _q574 = _q410 ^ len(_ak77)
    return _f48(*_a, **_k)
def _xn3080(_cs91):
    _r34 = (((((_cs91[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | ((_cs91[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF
    _tmp60 = (_cs91[1] << 17) & 0xFFFFFFFFFFFFFFFF
    _cs91[2] ^= _cs91[0]; _cs91[3] ^= _cs91[1]; _cs91[1] ^= _cs91[2]; _cs91[0] ^= _cs91[3]
    _cs91[2] ^= _tmp60; _cs91[3] = ((_cs91[3] << 45) | (_cs91[3] >> 19)) & 0xFFFFFFFFFFFFFFFF
    return _r34
def _xd3080(_v062, _v136, _k47):
    _delta20 = 0x9E3779B9; _s81 = (_delta20 * 32) & 0xFFFFFFFF
    for _ in range(32):
        _v136 = (_v136 - ((((_v062 << 4) ^ (_v062 >> 5)) + _v062) ^ (_s81 + _k47[(_s81 >> 11) & 3]))) & 0xFFFFFFFF
        _s81 = (_s81 - _delta20) & 0xFFFFFFFF
        _v062 = (_v062 - ((((_v136 << 4) ^ (_v136 >> 5)) + _v136) ^ (_s81 + _k47[_s81 & 3]))) & 0xFFFFFFFF
    return _v062, _v136
def _sh3080(_k47, _code21):
    _sv35 = [int.from_bytes(_k47[:8], 'little') ^ 0x736f6d6570736575, int.from_bytes(_k47[8:], 'little') ^ 0x646f72616e646f6d, int.from_bytes(_k47[:8], 'little') ^ 0x6c7967656e657261, int.from_bytes(_k47[8:], 'little') ^ 0x7465646279746573]
    def _sr():
        _sv35[0] = (_sv35[0] + _sv35[1]) & 0xFFFFFFFFFFFFFFFF; _sv35[1] = ((_sv35[1] << 13) | (_sv35[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ _sv35[0]; _sv35[0] = ((_sv35[0] << 32) | (_sv35[0] >> 32)) & 0xFFFFFFFFFFFFFFFF
        _sv35[2] = (_sv35[2] + _sv35[3]) & 0xFFFFFFFFFFFFFFFF; _sv35[3] = ((_sv35[3] << 16) | (_sv35[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ _sv35[2]
        _sv35[0] = (_sv35[0] + _sv35[3]) & 0xFFFFFFFFFFFFFFFF; _sv35[3] = ((_sv35[3] << 21) | (_sv35[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ _sv35[0]
        _sv35[2] = (_sv35[2] + _sv35[1]) & 0xFFFFFFFFFFFFFFFF; _sv35[1] = ((_sv35[1] << 17) | (_sv35[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ _sv35[2]; _sv35[2] = ((_sv35[2] << 32) | (_sv35[2] >> 32)) & 0xFFFFFFFFFFFFFFFF
    for _bi12 in range(0, len(_code21) - 7, 8):
        _tmp60 = int.from_bytes(_code21[_bi12:_bi12+8], 'little'); _sv35[3] ^= _tmp60; _sr(); _sr(); _sv35[0] ^= _tmp60
    _tmp60 = 0
    for _bi12 in range(len(_code21) & ~7, len(_code21)): _tmp60 |= _code21[_bi12] << (8 * (_bi12 & 7))
    _tmp60 |= (len(_code21) & 0xFF) << 56; _sv35[3] ^= _tmp60; _sr(); _sr(); _sv35[0] ^= _tmp60; _sv35[2] ^= 0xFF; _sr(); _sr(); _sr(); _sr()
    return (_sv35[0] ^ _sv35[1] ^ _sv35[2] ^ _sv35[3]) & 0xFFFFFFFFFFFFFFFF
def _vm3080(*_a78):
    _c1 = bytearray()
    _ek1 = (1047384561, 606262455, 2734661131, 1796152786)
    _ed1 = [155, 192, 173, 154, 29, 172, 213, 161]
    for _bi12 in range(0, len(_ed1), 8):
        _v062 = (_ed1[_bi12]<<24)|(_ed1[_bi12+1]<<16)|(_ed1[_bi12+2]<<8)|_ed1[_bi12+3]
        _v136 = (_ed1[_bi12+4]<<24)|(_ed1[_bi12+5]<<16)|(_ed1[_bi12+6]<<8)|_ed1[_bi12+7]
        _v062,_v136 = _xd3080(_v062,_v136,_ek1)
        _c1.extend([(_v062>>24)&0xFF,(_v062>>16)&0xFF,(_v062>>8)&0xFF,_v062&0xFF,(_v136>>24)&0xFF,(_v136>>16)&0xFF,(_v136>>8)&0xFF,_v136&0xFF])
    _c1 = _c1[:1]
    if _sh3080(b'\x90tP\xbd\xd7qW\xedW\xbb\xaaoj\xe8\xf2\n', bytes(_c1)) != 10606070715771882829: raise MemoryError()
    _cs1 = [11516978160209209534, 13010524639294431109, 9672801632940348984, 17956822576342608514]
    for _bi12 in range(len(_c1)): _c1[_bi12] ^= _xn3080(_cs1) & 0xFF
    _c2 = bytearray()
    _ek2 = (3791230043, 3405258719, 520298571, 937450684)
    _ed2 = [173, 98, 187, 94, 67, 18, 90, 200]
    for _bi12 in range(0, len(_ed2), 8):
        _v062 = (_ed2[_bi12]<<24)|(_ed2[_bi12+1]<<16)|(_ed2[_bi12+2]<<8)|_ed2[_bi12+3]
        _v136 = (_ed2[_bi12+4]<<24)|(_ed2[_bi12+5]<<16)|(_ed2[_bi12+6]<<8)|_ed2[_bi12+7]
        _v062,_v136 = _xd3080(_v062,_v136,_ek2)
        _c2.extend([(_v062>>24)&0xFF,(_v062>>16)&0xFF,(_v062>>8)&0xFF,_v062&0xFF,(_v136>>24)&0xFF,(_v136>>16)&0xFF,(_v136>>8)&0xFF,_v136&0xFF])
    _c2 = _c2[:1]
    if _sh3080(b'\x90tP\xbd\xd7qW\xedW\xbb\xaaoj\xe8\xf2\n', bytes(_c2)) != 11521267840597615028: raise MemoryError()
    _cs2 = [16991473895278689370, 12270112038571673357, 906265190742687588, 3183440977712232879]
    for _bi12 in range(len(_c2)): _c2[_bi12] ^= _xn3080(_cs2) & 0xFF
    _c3 = bytearray()
    _ek3 = (1224806606, 3719594044, 557565455, 865330025)
    _ed3 = [203, 151, 229, 182, 8, 253, 119, 201]
    for _bi12 in range(0, len(_ed3), 8):
        _v062 = (_ed3[_bi12]<<24)|(_ed3[_bi12+1]<<16)|(_ed3[_bi12+2]<<8)|_ed3[_bi12+3]
        _v136 = (_ed3[_bi12+4]<<24)|(_ed3[_bi12+5]<<16)|(_ed3[_bi12+6]<<8)|_ed3[_bi12+7]
        _v062,_v136 = _xd3080(_v062,_v136,_ek3)
        _c3.extend([(_v062>>24)&0xFF,(_v062>>16)&0xFF,(_v062>>8)&0xFF,_v062&0xFF,(_v136>>24)&0xFF,(_v136>>16)&0xFF,(_v136>>8)&0xFF,_v136&0xFF])
    _c3 = _c3[:1]
    if _sh3080(b'\x90tP\xbd\xd7qW\xedW\xbb\xaaoj\xe8\xf2\n', bytes(_c3)) != 8666096691433314859: raise MemoryError()
    _cs3 = [9830536885785154556, 12341858018755671816, 2278072034567012728, 9445674662322017007]
    for _bi12 in range(len(_c3)): _c3[_bi12] ^= _xn3080(_cs3) & 0xFF
    _c0 = bytearray()
    _ek0 = (103239053, 1181763986, 4292216113, 1097564147)
    _ed0 = [6, 5, 151, 137, 162, 148, 90, 235, 183, 213, 62, 182, 39, 221, 60, 121, 93, 147, 194, 245, 227, 120, 135, 109, 77, 45, 80, 67, 105, 166, 187, 228, 175, 41, 163, 24, 170, 141, 16, 83, 252, 10, 247, 26, 72, 147, 151, 13, 247, 26, 220, 255, 106, 161, 19, 40, 123, 159, 3, 42, 34, 14, 199, 110, 230, 106, 242, 209, 247, 218, 155, 247, 160, 51, 76, 108, 164, 148, 126, 60]
    for _bi12 in range(0, len(_ed0), 8):
        _v062 = (_ed0[_bi12]<<24)|(_ed0[_bi12+1]<<16)|(_ed0[_bi12+2]<<8)|_ed0[_bi12+3]
        _v136 = (_ed0[_bi12+4]<<24)|(_ed0[_bi12+5]<<16)|(_ed0[_bi12+6]<<8)|_ed0[_bi12+7]
        _v062,_v136 = _xd3080(_v062,_v136,_ek0)
        _c0.extend([(_v062>>24)&0xFF,(_v062>>16)&0xFF,(_v062>>8)&0xFF,_v062&0xFF,(_v136>>24)&0xFF,(_v136>>16)&0xFF,(_v136>>8)&0xFF,_v136&0xFF])
    _c0 = _c0[:79]
    if _sh3080(b'\x90tP\xbd\xd7qW\xedW\xbb\xaaoj\xe8\xf2\n', bytes(_c0)) != 16494333842725159113: raise MemoryError()
    _cs0 = [11692906694787888152, 12884486652105043807, 7774354054860225607, 4366306485966090034]
    for _bi12 in range(len(_c0)): _c0[_bi12] ^= _xn3080(_cs0) & 0xFF
    _c4 = bytearray()
    _ek4 = (4240654700, 3074397996, 1584156212, 789703253)
    _ed4 = [105, 59, 50, 116, 122, 140, 60, 145]
    for _bi12 in range(0, len(_ed4), 8):
        _v062 = (_ed4[_bi12]<<24)|(_ed4[_bi12+1]<<16)|(_ed4[_bi12+2]<<8)|_ed4[_bi12+3]
        _v136 = (_ed4[_bi12+4]<<24)|(_ed4[_bi12+5]<<16)|(_ed4[_bi12+6]<<8)|_ed4[_bi12+7]
        _v062,_v136 = _xd3080(_v062,_v136,_ek4)
        _c4.extend([(_v062>>24)&0xFF,(_v062>>16)&0xFF,(_v062>>8)&0xFF,_v062&0xFF,(_v136>>24)&0xFF,(_v136>>16)&0xFF,(_v136>>8)&0xFF,_v136&0xFF])
    _shared34 = [[] for _ in range(3)]
    _gregs86 = [None] * 4
    _loc60 = list(_a78[:2]) + [None] * 0
    _consts75 = [6528, 6527, 2, 3, 6773]
    _names21 = []
    _gl39 = globals()
    _gl39.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))
    _ot0 = [140, 197, 203, 231, 98, 52, 165, 246, 251, 155, 142, 72, 224, 75, 150, 154, 240, 236, 42, 62, 120, 83, 153, 4, 116, 229, 112, 28, 104, 84, 80, 87, 88, 149, 215, 35, 173, 96, 71, 117, 59, 233, 132, 178, 26, 118, 3, 160, 131, 24, 31, 136, 201, 47, 134, 192, 180, 152, 239, 200, 179, 122, 70, 226, 106, 51, 144, 198, 55, 18, 34, 102, 141, 254, 163, 125, 204, 174, 81, 137, 148, 5, 171, 223, 168, 14, 158, 65, 21, 207, 249, 195, 73, 13, 100, 32, 162, 43, 68, 209, 238, 17, 8, 182, 167, 221, 235, 121, 210, 109, 49, 196, 133, 82, 247, 78, 183, 205, 124, 161, 63, 16, 85, 222, 151, 177, 57, 22, 27, 29, 95, 157, 242, 97, 206, 1, 146, 38, 130, 9, 89, 7, 208, 20, 230, 176, 108, 245, 199, 50, 69, 77, 244, 46, 79, 191, 147, 101, 25, 159, 248, 213, 37, 99, 252, 138, 145, 67, 241, 110, 187, 39, 164, 127, 143, 86, 243, 214, 119, 93, 45, 12, 190, 10, 74, 216, 255, 139, 156, 58, 113, 115, 60, 30, 76, 250, 128, 44, 228, 220, 232, 103, 184, 185, 202, 41, 227, 6, 253, 2, 218, 170, 23, 219, 15, 211, 188, 217, 181, 36, 193, 53, 48, 237, 186, 107, 166, 61, 126, 0, 129, 111, 175, 94, 123, 172, 40, 169, 194, 66, 64, 11, 234, 56, 114, 225, 19, 92, 105, 212, 135, 189, 54, 91, 90, 33]
    _stk0 = []
    _pc0 = 0
    _regs0 = [None] * 8
    _eh0 = []
    _ns0 = {}
    exec(bytes(b^187 for b in [223, 222, 221, 155, 228, 211, 221, 139, 228, 139, 147, 200, 151, 215, 151, 216, 151, 213, 151, 220, 151, 223, 151, 203, 151, 201, 151, 211, 151, 195, 146, 129, 177, 155, 200, 149, 218, 203, 203, 222, 213, 223, 147, 200, 224, 150, 138, 230, 146, 128, 201, 222, 207, 206, 201, 213, 155, 203, 144, 138, 177, 223, 222, 221, 155, 228, 211, 221, 139, 228, 138, 147, 200, 151, 215, 151, 216, 151, 213, 151, 220, 151, 223, 151, 203, 151, 201, 151, 211, 151, 195, 146, 129, 177, 155, 200, 149, 218, 203, 203, 222, 213, 223, 147, 197, 200, 149, 203, 212, 203, 147, 146, 146, 128, 201, 222, 207, 206, 201, 213, 155, 203, 144, 138, 177, 223, 222, 221, 155, 228, 211, 221, 139, 228, 137, 147, 200, 151, 215, 151, 216, 151, 213, 151, 220, 151, 223, 151, 203, 151, 201, 151, 211, 151, 195, 146, 129, 177, 155, 220, 224, 213, 224, 223, 224, 203, 144, 138, 230, 230, 230, 134, 200, 149, 203, 212, 203, 147, 146, 128, 201, 222, 207, 206, 201, 213, 155, 203, 144, 137, 177]).decode(),_ns0)
    _dh0 = {6: _ns0['_hf0_0'], 33: _ns0['_hf0_1'], 5: _ns0['_hf0_2']}
    _ot1 = [44, 106, 150, 180, 227, 152, 163, 166, 243, 138, 43, 132, 149, 12, 83, 123, 247, 81, 25, 41, 64, 18, 185, 240, 190, 168, 124, 75, 239, 228, 200, 235, 159, 174, 218, 108, 217, 21, 241, 103, 182, 70, 142, 100, 84, 196, 93, 170, 120, 101, 216, 95, 154, 249, 49, 245, 72, 165, 91, 130, 59, 193, 187, 250, 246, 53, 133, 208, 205, 213, 0, 79, 203, 5, 88, 220, 19, 50, 231, 112, 82, 32, 175, 171, 135, 22, 78, 2, 69, 52, 140, 60, 65, 210, 24, 237, 8, 214, 131, 176, 191, 54, 46, 113, 51, 89, 30, 85, 153, 248, 58, 34, 195, 3, 86, 238, 204, 33, 102, 92, 7, 254, 127, 233, 206, 232, 178, 39, 198, 188, 99, 212, 207, 20, 128, 76, 111, 115, 126, 35, 38, 110, 114, 94, 192, 29, 151, 137, 215, 55, 244, 183, 181, 26, 134, 97, 48, 189, 156, 1, 42, 229, 197, 184, 169, 6, 148, 61, 194, 98, 10, 57, 104, 40, 63, 125, 145, 74, 118, 226, 199, 172, 129, 77, 173, 177, 209, 162, 219, 121, 45, 4, 68, 9, 222, 230, 157, 31, 109, 221, 160, 116, 143, 155, 255, 16, 66, 224, 253, 105, 17, 136, 158, 62, 96, 122, 47, 71, 147, 14, 56, 202, 225, 90, 80, 67, 223, 23, 28, 141, 139, 211, 242, 15, 167, 252, 27, 186, 13, 251, 119, 37, 11, 146, 107, 144, 234, 73, 36, 87, 236, 201, 117, 179, 161, 164]
    _stk1 = []
    _pc1 = 0
    _regs1 = [None] * 8
    _eh1 = []
    _dh1 = {}
    _ot2 = [100, 159, 83, 54, 125, 89, 45, 86, 118, 176, 3, 217, 25, 238, 234, 236, 42, 220, 194, 44, 120, 51, 21, 30, 23, 129, 167, 254, 169, 204, 158, 228, 216, 210, 147, 34, 155, 56, 207, 219, 160, 225, 116, 151, 74, 206, 255, 102, 114, 187, 179, 195, 38, 37, 62, 132, 203, 163, 148, 124, 188, 98, 58, 73, 14, 72, 29, 252, 68, 197, 15, 55, 31, 227, 250, 224, 212, 43, 154, 242, 183, 196, 170, 8, 105, 13, 208, 2, 108, 70, 0, 52, 5, 186, 245, 189, 193, 76, 249, 87, 7, 96, 205, 141, 213, 49, 12, 41, 247, 168, 137, 201, 232, 229, 97, 59, 82, 90, 136, 144, 138, 190, 20, 66, 223, 18, 172, 75, 64, 253, 241, 111, 36, 50, 133, 123, 103, 235, 150, 69, 246, 162, 121, 248, 153, 115, 110, 135, 215, 67, 149, 174, 33, 200, 11, 113, 48, 156, 112, 19, 165, 104, 61, 221, 117, 240, 192, 80, 140, 185, 230, 17, 191, 63, 81, 122, 6, 178, 77, 60, 211, 24, 71, 53, 199, 109, 94, 22, 226, 218, 214, 39, 171, 84, 134, 65, 131, 142, 182, 40, 106, 78, 166, 244, 222, 237, 157, 239, 173, 161, 126, 79, 202, 9, 26, 47, 91, 164, 101, 180, 184, 99, 130, 119, 4, 145, 175, 1, 85, 143, 32, 46, 152, 88, 198, 95, 57, 181, 92, 251, 27, 16, 243, 233, 231, 209, 177, 139, 107, 127, 93, 35, 128, 10, 146, 28]
    _stk2 = []
    _pc2 = 0
    _regs2 = [None] * 8
    _eh2 = []
    _dh2 = {}
    _ot3 = [208, 94, 193, 113, 30, 251, 151, 191, 21, 115, 45, 181, 95, 148, 227, 57, 176, 16, 249, 214, 92, 110, 185, 224, 2, 72, 83, 90, 204, 145, 23, 206, 99, 232, 189, 89, 15, 143, 166, 70, 27, 167, 154, 4, 101, 146, 87, 196, 177, 119, 179, 14, 198, 48, 102, 6, 182, 199, 230, 84, 62, 243, 39, 223, 52, 111, 122, 55, 247, 215, 78, 205, 126, 85, 149, 93, 67, 245, 54, 81, 142, 253, 248, 59, 236, 22, 36, 217, 46, 105, 66, 170, 203, 125, 130, 56, 75, 184, 209, 213, 220, 108, 173, 37, 183, 109, 155, 112, 124, 19, 34, 207, 160, 178, 80, 188, 97, 219, 190, 32, 74, 5, 246, 164, 127, 234, 118, 174, 131, 159, 0, 238, 195, 24, 77, 18, 210, 1, 135, 8, 197, 237, 13, 136, 216, 231, 9, 43, 222, 69, 201, 82, 10, 98, 25, 152, 44, 252, 221, 41, 186, 96, 47, 235, 7, 49, 61, 31, 172, 212, 169, 139, 163, 254, 171, 158, 150, 38, 123, 229, 128, 180, 58, 200, 162, 63, 161, 157, 51, 76, 133, 120, 255, 194, 91, 240, 17, 132, 121, 86, 114, 71, 140, 73, 175, 64, 117, 228, 28, 60, 42, 141, 233, 11, 226, 79, 26, 104, 103, 53, 3, 20, 107, 250, 68, 100, 202, 106, 50, 218, 168, 116, 134, 12, 35, 242, 153, 65, 225, 147, 40, 156, 29, 144, 192, 88, 129, 244, 165, 33, 211, 241, 239, 137, 187, 138]
    _stk3 = []
    _pc3 = 0
    _regs3 = [None] * 8
    _eh3 = []
    _dh3 = {}
    _tc85 = __import__('time').perf_counter_ns
    _segs = [(0, 18)]
    _tprev = _tc85()
    _ck75 = [34]
    _si61 = 0
    for _seg_vm26, _seg_n41 in _segs:
        _td63 = _tc85() - _tprev
        if _td63 > 5000000000: return None
        _tprev = _tc85()
        if _seg_vm26 == 0:
            _ic0 = 0
            while _pc0 < len(_c0):
              try:
                _ic0 += 1
                _op23 = _ot0[_c0[_pc0] & 0xFF]
                if _op23 in _dh0:
                    _pc0 = _dh0[_op23](_stk0, _loc60, _consts75, _names21, _gl39, _c0, _pc0, _regs0, _shared34, _gregs86)
                    continue
                _ha086 = [255, 0, 1, 2, 3, 255, 255, 4, 5, 255, 255, 255, 255, 255, 255, 255, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 255, 255, 255, 255, 255, 17, 255, 18, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 19, 20, 21, 22, 23, 24, 25, 26, 27, 255, 255, 255, 255, 255, 255, 255, 28, 29, 30, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 255, 255, 255, 255, 255, 42, 43, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 44, 255, 255, 255, 255, 255, 255, 255, 45, 46, 47, 255, 255, 255, 255, 255, 48, 49, 50, 51, 52, 53, 54, 255, 255, 255, 255, 255, 255, 255, 255, 255, 55, 56, 57, 58, 59, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 60, 61, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 62, 63]
                _ai031 = _ha086[_op23]
                if _ai031 == 0:
                    _stk0.append(_consts75[_c0[_pc0+1]]); _pc0 += 2
                elif _ai031 == 1:
                    _stk0.append(_loc60[_c0[_pc0+1]]); _pc0 += 2
                elif _ai031 == 2:
                    _loc60[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _ai031 == 3:
                    _stk0.append(_gl39[_names21[_c0[_pc0+1]]]); _pc0 += 2
                elif _ai031 == 4:
                    _stk0.pop(); _pc0 += 1
                elif _ai031 == 5:
                    _stk0[-1], _stk0[-2] = _stk0[-2], _stk0[-1]; _pc0 += 1
                elif _ai031 == 6:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 + _b89); _pc0 += 1
                elif _ai031 == 7:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 - _b89); _pc0 += 1
                elif _ai031 == 8:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 * _b89); _pc0 += 1
                elif _ai031 == 9:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 % _b89); _pc0 += 1
                elif _ai031 == 10:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 // _b89); _pc0 += 1
                elif _ai031 == 11:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 ** _b89); _pc0 += 1
                elif _ai031 == 12:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 ^ _b89); _pc0 += 1
                elif _ai031 == 13:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 & _b89); _pc0 += 1
                elif _ai031 == 14:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 | _b89); _pc0 += 1
                elif _ai031 == 15:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 << _b89); _pc0 += 1
                elif _ai031 == 16:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 >> _b89); _pc0 += 1
                elif _ai031 == 17:
                    _stk0.append(-_stk0.pop()); _pc0 += 1
                elif _ai031 == 18:
                    _stk0.append(not _stk0.pop()); _pc0 += 1
                elif _ai031 == 19:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 == _b89); _pc0 += 1
                elif _ai031 == 20:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 != _b89); _pc0 += 1
                elif _ai031 == 21:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 < _b89); _pc0 += 1
                elif _ai031 == 22:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 > _b89); _pc0 += 1
                elif _ai031 == 23:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 <= _b89); _pc0 += 1
                elif _ai031 == 24:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 >= _b89); _pc0 += 1
                elif _ai031 == 25:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 is _b89); _pc0 += 1
                elif _ai031 == 26:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 is not _b89); _pc0 += 1
                elif _ai031 == 27:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78 in _b89); _pc0 += 1
                elif _ai031 == 28:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                elif _ai031 == 29:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if _stk0.pop() else _pc0 + 3
                elif _ai031 == 30:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if not _stk0.pop() else _pc0 + 3
                elif _ai031 == 31:
                    _tmp60 = _c0[_pc0+1]
                    if _tmp60: _val22 = _stk0[-_tmp60:]; del _stk0[-_tmp60:]
                    else: _val22 = []
                    _stk0.append(_stk0.pop()(*_val22)); _pc0 += 2
                elif _ai031 == 32:
                    _stk0.append(getattr(_stk0.pop(), _names21[_c0[_pc0+1]])); _pc0 += 2
                elif _ai031 == 33:
                    _val22 = _stk0.pop(); setattr(_stk0.pop(), _names21[_c0[_pc0+1]], _val22); _pc0 += 2
                elif _ai031 == 34:
                    _tmp60 = _c0[_pc0+2]
                    _val22 = [_stk0.pop() for _ in range(_tmp60)][::-1]
                    _stk0.append(getattr(_stk0.pop(), _names21[_c0[_pc0+1]])(*_val22)); _pc0 += 3
                elif _ai031 == 35:
                    _tmp60 = _c0[_pc0+1]
                    if _tmp60: _val22 = _stk0[-_tmp60:]; del _stk0[-_tmp60:]
                    else: _val22 = []
                    _stk0.append(_val22); _pc0 += 2
                elif _ai031 == 36:
                    _tmp60 = _c0[_pc0+1]
                    if _tmp60: _val22 = tuple(_stk0[-_tmp60:]); del _stk0[-_tmp60:]
                    else: _val22 = ()
                    _stk0.append(_val22); _pc0 += 2
                elif _ai031 == 37:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(_a78[_b89]); _pc0 += 1
                elif _ai031 == 38:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _val22 = _stk0.pop(); _a78[_b89] = _val22; _pc0 += 1
                elif _ai031 == 39:
                    _val22 = list(_stk0.pop())[:_c0[_pc0+1]]; _stk0.extend(reversed(_val22)); _pc0 += 2
                elif _ai031 == 40:
                    _tmp60 = _c0[_pc0+1]; _val22 = {}
                    for _ in range(_tmp60): _b89 = _stk0.pop(); _a78 = _stk0.pop(); _val22[_a78] = _b89
                    _stk0.append(_val22); _pc0 += 2
                elif _ai031 == 41:
                    _b89 = _stk0.pop(); _a78 = _stk0.pop(); _stk0.append(slice(_a78, _b89)); _pc0 += 1
                elif _ai031 == 42:
                    _stk0.append(iter(_stk0.pop())); _pc0 += 1
                elif _ai031 == 43:
                    _val22 = next(_stk0[-1], None)
                    if _val22 is None: _stk0.pop(); _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                    else: _stk0.append(_val22); _pc0 += 3
                elif _ai031 == 44:
                    return _stk0.pop()
                elif _ai031 == 45:
                    _eh0.append(_c0[_pc0+1] | (_c0[_pc0+2] << 8)); _pc0 += 3
                elif _ai031 == 46:
                    _eh0.pop(); _pc0 += 1
                elif _ai031 == 47:
                    _tmp60 = _c0[_pc0+1] | (_c0[_pc0+2] << 8); _c0[_tmp60] ^= _c0[_pc0+3]; _pc0 += 4
                elif _ai031 == 48:
                    _regs0[_c0[_pc0+1]] = _loc60[_c0[_pc0+2]]; _pc0 += 3
                elif _ai031 == 49:
                    _loc60[_c0[_pc0+2]] = _regs0[_c0[_pc0+1]]; _pc0 += 3
                elif _ai031 == 50:
                    _stk0.append(_regs0[_c0[_pc0+1]]); _pc0 += 2
                elif _ai031 == 51:
                    _regs0[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _ai031 == 52:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _ai031 == 53:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] + _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _ai031 == 54:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] - _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _ai031 == 55:
                    _shared34[_c0[_pc0+1]].append(_stk0.pop()); _pc0 += 2
                elif _ai031 == 56:
                    _stk0.append(_shared34[_c0[_pc0+1]].pop()); _pc0 += 2
                elif _ai031 == 57:
                    _gregs86[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _ai031 == 58:
                    _stk0.append(_gregs86[_c0[_pc0+1]]); _pc0 += 2
                elif _ai031 == 59:
                    _pc0 += 1; break
                elif _ai031 == 60:
                    _stk0.append(_stk0[-1]); _loc60[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _ai031 == 61:
                    _stk0.append(_loc60[_c0[_pc0+1]]); _stk0.append(_loc60[_c0[_pc0+2]]); _pc0 += 3
                elif _ai031 == 62:
                    _pc0 += 1
                elif _ai031 == 63:
                    return _stk0[-1] if _stk0 else None
                else: _pc0 += 1
              except Exception as _exc:
                if _eh0: _pc0 = _eh0.pop(); _stk0.append(_exc)
                else: raise
        elif _seg_vm26 == 1:
            _ic1 = 0
            while _pc1 < len(_c1):
              try:
                _ic1 += 1
                _op23 = _ot1[_c1[_pc1] & 0xFF]
                if _op23 < 66:
                    if _op23 < 24:
                        if _op23 < 16:
                            if _op23 < 5:
                                if _op23 < 3:
                                    if _op23 < 2:
                                        if _op23 == 1:
                                            _stk1.append(_consts75[_c1[_pc1+1]]); _pc1 += 2
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 2:
                                            _stk1.append(_loc60[_c1[_pc1+1]]); _pc1 += 2
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 4:
                                        if _op23 == 3:
                                            _loc60[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 4:
                                            _stk1.append(_gl39[_names21[_c1[_pc1+1]]]); _pc1 += 2
                                        else: _pc1 += 1
                            else:
                                if _op23 < 7:
                                    if _op23 < 6:
                                        if _op23 == 5:
                                            _gl39[_names21[_c1[_pc1+1]]] = _stk1.pop(); _pc1 += 2
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 6:
                                            _stk1.append(_stk1[-1]); _pc1 += 1
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 8:
                                        if _op23 == 7:
                                            _stk1.pop(); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 8:
                                            _stk1[-1], _stk1[-2] = _stk1[-2], _stk1[-1]; _pc1 += 1
                                        else: _pc1 += 1
                        else:
                            if _op23 < 20:
                                if _op23 < 18:
                                    if _op23 < 17:
                                        if _op23 == 16:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 + _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 17:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 - _b89); _pc1 += 1
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 19:
                                        if _op23 == 18:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 * _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 19:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 % _b89); _pc1 += 1
                                        else: _pc1 += 1
                            else:
                                if _op23 < 22:
                                    if _op23 < 21:
                                        if _op23 == 20:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 // _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 21:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 ** _b89); _pc1 += 1
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 23:
                                        if _op23 == 22:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 ^ _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 23:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 & _b89); _pc1 += 1
                                        else: _pc1 += 1
                    else:
                        if _op23 < 50:
                            if _op23 < 33:
                                if _op23 < 26:
                                    if _op23 < 25:
                                        if _op23 == 24:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 | _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 25:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 << _b89); _pc1 += 1
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 32:
                                        if _op23 == 26:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 >> _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 32:
                                            _stk1.append(-_stk1.pop()); _pc1 += 1
                                        else: _pc1 += 1
                            else:
                                if _op23 < 48:
                                    if _op23 < 34:
                                        if _op23 == 33:
                                            _stk1.append(~_stk1.pop()); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 34:
                                            _stk1.append(not _stk1.pop()); _pc1 += 1
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 49:
                                        if _op23 == 48:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 == _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 49:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 != _b89); _pc1 += 1
                                        else: _pc1 += 1
                        else:
                            if _op23 < 54:
                                if _op23 < 52:
                                    if _op23 < 51:
                                        if _op23 == 50:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 < _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 51:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 > _b89); _pc1 += 1
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 53:
                                        if _op23 == 52:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 <= _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 53:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 >= _b89); _pc1 += 1
                                        else: _pc1 += 1
                            else:
                                if _op23 < 56:
                                    if _op23 < 55:
                                        if _op23 == 54:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 is _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 55:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 is not _b89); _pc1 += 1
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 64:
                                        if _op23 == 56:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78 in _b89); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 < 65:
                                            if _op23 == 64:
                                                _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                                            else: _pc1 += 1
                                        else:
                                            if _op23 == 65:
                                                _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if _stk1.pop() else _pc1 + 3
                                            else: _pc1 += 1
                else:
                    if _op23 < 122:
                        if _op23 < 87:
                            if _op23 < 83:
                                if _op23 < 81:
                                    if _op23 < 80:
                                        if _op23 == 66:
                                            _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if not _stk1.pop() else _pc1 + 3
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 80:
                                            _tmp60 = _c1[_pc1+1]
                                            if _tmp60: _val22 = _stk1[-_tmp60:]; del _stk1[-_tmp60:]
                                            else: _val22 = []
                                            _stk1.append(_stk1.pop()(*_val22)); _pc1 += 2
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 82:
                                        if _op23 == 81:
                                            _stk1.append(getattr(_stk1.pop(), _names21[_c1[_pc1+1]])); _pc1 += 2
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 82:
                                            _val22 = _stk1.pop(); setattr(_stk1.pop(), _names21[_c1[_pc1+1]], _val22); _pc1 += 2
                                        else: _pc1 += 1
                            else:
                                if _op23 < 85:
                                    if _op23 < 84:
                                        if _op23 == 83:
                                            _tmp60 = _c1[_pc1+2]
                                            _val22 = [_stk1.pop() for _ in range(_tmp60)][::-1]
                                            _stk1.append(getattr(_stk1.pop(), _names21[_c1[_pc1+1]])(*_val22)); _pc1 += 3
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 84:
                                            _tmp60 = _c1[_pc1+1]
                                            if _tmp60: _val22 = _stk1[-_tmp60:]; del _stk1[-_tmp60:]
                                            else: _val22 = []
                                            _stk1.append(_val22); _pc1 += 2
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 86:
                                        if _op23 == 85:
                                            _tmp60 = _c1[_pc1+1]
                                            if _tmp60: _val22 = tuple(_stk1[-_tmp60:]); del _stk1[-_tmp60:]
                                            else: _val22 = ()
                                            _stk1.append(_val22); _pc1 += 2
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 86:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(_a78[_b89]); _pc1 += 1
                                        else: _pc1 += 1
                        else:
                            if _op23 < 96:
                                if _op23 < 89:
                                    if _op23 < 88:
                                        if _op23 == 87:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _val22 = _stk1.pop(); _a78[_b89] = _val22; _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 88:
                                            _val22 = list(_stk1.pop())[:_c1[_pc1+1]]; _stk1.extend(reversed(_val22)); _pc1 += 2
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 90:
                                        if _op23 == 89:
                                            _tmp60 = _c1[_pc1+1]; _val22 = {}
                                            for _ in range(_tmp60): _b89 = _stk1.pop(); _a78 = _stk1.pop(); _val22[_a78] = _b89
                                            _stk1.append(_val22); _pc1 += 2
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 90:
                                            _b89 = _stk1.pop(); _a78 = _stk1.pop(); _stk1.append(slice(_a78, _b89)); _pc1 += 1
                                        else: _pc1 += 1
                            else:
                                if _op23 < 112:
                                    if _op23 < 97:
                                        if _op23 == 96:
                                            _stk1.append(iter(_stk1.pop())); _pc1 += 1
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 97:
                                            _val22 = next(_stk1[-1], None)
                                            if _val22 is None: _stk1.pop(); _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                                            else: _stk1.append(_val22); _pc1 += 3
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 120:
                                        if _op23 == 112:
                                            return _stk1.pop()
                                        else: _pc1 += 1
                                    else:
                                        if _op23 < 121:
                                            if _op23 == 120:
                                                _eh1.append(_c1[_pc1+1] | (_c1[_pc1+2] << 8)); _pc1 += 3
                                            else: _pc1 += 1
                                        else:
                                            if _op23 == 121:
                                                _eh1.pop(); _pc1 += 1
                                            else: _pc1 += 1
                    else:
                        if _op23 < 144:
                            if _op23 < 131:
                                if _op23 < 129:
                                    if _op23 < 128:
                                        if _op23 == 122:
                                            _tmp60 = _c1[_pc1+1] | (_c1[_pc1+2] << 8); _c1[_tmp60] ^= _c1[_pc1+3]; _pc1 += 4
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 128:
                                            _regs1[_c1[_pc1+1]] = _loc60[_c1[_pc1+2]]; _pc1 += 3
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 130:
                                        if _op23 == 129:
                                            _loc60[_c1[_pc1+2]] = _regs1[_c1[_pc1+1]]; _pc1 += 3
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 130:
                                            _stk1.append(_regs1[_c1[_pc1+1]]); _pc1 += 2
                                        else: _pc1 += 1
                            else:
                                if _op23 < 133:
                                    if _op23 < 132:
                                        if _op23 == 131:
                                            _regs1[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 132:
                                            _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+2]]; _pc1 += 3
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 134:
                                        if _op23 == 133:
                                            _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] + _regs1[_c1[_pc1+2]]; _pc1 += 3
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 134:
                                            _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] - _regs1[_c1[_pc1+2]]; _pc1 += 3
                                        else: _pc1 += 1
                        else:
                            if _op23 < 148:
                                if _op23 < 146:
                                    if _op23 < 145:
                                        if _op23 == 144:
                                            _shared34[_c1[_pc1+1]].append(_stk1.pop()); _pc1 += 2
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 145:
                                            _stk1.append(_shared34[_c1[_pc1+1]].pop()); _pc1 += 2
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 147:
                                        if _op23 == 146:
                                            _gregs86[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 147:
                                            _stk1.append(_gregs86[_c1[_pc1+1]]); _pc1 += 2
                                        else: _pc1 += 1
                            else:
                                if _op23 < 161:
                                    if _op23 < 160:
                                        if _op23 == 148:
                                            _pc1 += 1; break
                                        else: _pc1 += 1
                                    else:
                                        if _op23 == 160:
                                            _stk1.append(_stk1[-1]); _loc60[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                                        else: _pc1 += 1
                                else:
                                    if _op23 < 254:
                                        if _op23 == 161:
                                            _stk1.append(_loc60[_c1[_pc1+1]]); _stk1.append(_loc60[_c1[_pc1+2]]); _pc1 += 3
                                        else: _pc1 += 1
                                    else:
                                        if _op23 < 255:
                                            if _op23 == 254:
                                                _pc1 += 1
                                            else: _pc1 += 1
                                        else:
                                            if _op23 == 255:
                                                return _stk1[-1] if _stk1 else None
                                            else: _pc1 += 1
              except Exception as _exc:
                if _eh1: _pc1 = _eh1.pop(); _stk1.append(_exc)
                else: raise
        elif _seg_vm26 == 2:
            _ic2 = 0
            while _pc2 < len(_c2):
              try:
                _ic2 += 1
                _op23 = _ot2[_c2[_pc2] & 0xFF]
                if _op23 == 1:
                    _stk2.append(_consts75[_c2[_pc2+1]]); _pc2 += 2
                elif _op23 == 2:
                    _stk2.append(_loc60[_c2[_pc2+1]]); _pc2 += 2
                elif _op23 == 3:
                    _loc60[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _op23 == 4:
                    _stk2.append(_gl39[_names21[_c2[_pc2+1]]]); _pc2 += 2
                elif _op23 == 5:
                    _gl39[_names21[_c2[_pc2+1]]] = _stk2.pop(); _pc2 += 2
                elif _op23 == 6:
                    _stk2.append(_stk2[-1]); _pc2 += 1
                elif _op23 == 7:
                    _stk2.pop(); _pc2 += 1
                elif _op23 == 8:
                    _stk2[-1], _stk2[-2] = _stk2[-2], _stk2[-1]; _pc2 += 1
                elif _op23 == 16:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 + _b89); _pc2 += 1
                elif _op23 == 17:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 - _b89); _pc2 += 1
                elif _op23 == 18:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 * _b89); _pc2 += 1
                elif _op23 == 19:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 % _b89); _pc2 += 1
                elif _op23 == 20:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 // _b89); _pc2 += 1
                elif _op23 == 21:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 ** _b89); _pc2 += 1
                elif _op23 == 22:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 ^ _b89); _pc2 += 1
                elif _op23 == 23:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 & _b89); _pc2 += 1
                elif _op23 == 24:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 | _b89); _pc2 += 1
                elif _op23 == 25:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 << _b89); _pc2 += 1
                elif _op23 == 26:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 >> _b89); _pc2 += 1
                elif _op23 == 32:
                    _stk2.append(-_stk2.pop()); _pc2 += 1
                elif _op23 == 33:
                    _stk2.append(~_stk2.pop()); _pc2 += 1
                elif _op23 == 34:
                    _stk2.append(not _stk2.pop()); _pc2 += 1
                elif _op23 == 48:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 == _b89); _pc2 += 1
                elif _op23 == 49:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 != _b89); _pc2 += 1
                elif _op23 == 50:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 < _b89); _pc2 += 1
                elif _op23 == 51:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 > _b89); _pc2 += 1
                elif _op23 == 52:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 <= _b89); _pc2 += 1
                elif _op23 == 53:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 >= _b89); _pc2 += 1
                elif _op23 == 54:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 is _b89); _pc2 += 1
                elif _op23 == 55:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 is not _b89); _pc2 += 1
                elif _op23 == 56:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78 in _b89); _pc2 += 1
                elif _op23 == 64:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                elif _op23 == 65:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if _stk2.pop() else _pc2 + 3
                elif _op23 == 66:
                    _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if not _stk2.pop() else _pc2 + 3
                elif _op23 == 80:
                    _tmp60 = _c2[_pc2+1]
                    if _tmp60: _val22 = _stk2[-_tmp60:]; del _stk2[-_tmp60:]
                    else: _val22 = []
                    _stk2.append(_stk2.pop()(*_val22)); _pc2 += 2
                elif _op23 == 81:
                    _stk2.append(getattr(_stk2.pop(), _names21[_c2[_pc2+1]])); _pc2 += 2
                elif _op23 == 82:
                    _val22 = _stk2.pop(); setattr(_stk2.pop(), _names21[_c2[_pc2+1]], _val22); _pc2 += 2
                elif _op23 == 83:
                    _tmp60 = _c2[_pc2+2]
                    _val22 = [_stk2.pop() for _ in range(_tmp60)][::-1]
                    _stk2.append(getattr(_stk2.pop(), _names21[_c2[_pc2+1]])(*_val22)); _pc2 += 3
                elif _op23 == 84:
                    _tmp60 = _c2[_pc2+1]
                    if _tmp60: _val22 = _stk2[-_tmp60:]; del _stk2[-_tmp60:]
                    else: _val22 = []
                    _stk2.append(_val22); _pc2 += 2
                elif _op23 == 85:
                    _tmp60 = _c2[_pc2+1]
                    if _tmp60: _val22 = tuple(_stk2[-_tmp60:]); del _stk2[-_tmp60:]
                    else: _val22 = ()
                    _stk2.append(_val22); _pc2 += 2
                elif _op23 == 86:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(_a78[_b89]); _pc2 += 1
                elif _op23 == 87:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _val22 = _stk2.pop(); _a78[_b89] = _val22; _pc2 += 1
                elif _op23 == 88:
                    _val22 = list(_stk2.pop())[:_c2[_pc2+1]]; _stk2.extend(reversed(_val22)); _pc2 += 2
                elif _op23 == 89:
                    _tmp60 = _c2[_pc2+1]
                    _val22 = {}
                    for _ in range(_tmp60): _b89 = _stk2.pop(); _a78 = _stk2.pop(); _val22[_a78] = _b89
                    _stk2.append(_val22); _pc2 += 2
                elif _op23 == 90:
                    _b89 = _stk2.pop(); _a78 = _stk2.pop(); _stk2.append(slice(_a78, _b89)); _pc2 += 1
                elif _op23 == 96:
                    _stk2.append(iter(_stk2.pop())); _pc2 += 1
                elif _op23 == 97:
                    _val22 = next(_stk2[-1], None)
                    if _val22 is None: _stk2.pop(); _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                    else: _stk2.append(_val22); _pc2 += 3
                elif _op23 == 112:
                    return _stk2.pop()
                elif _op23 == 120:
                    _eh2.append(_c2[_pc2+1] | (_c2[_pc2+2] << 8)); _pc2 += 3
                elif _op23 == 121:
                    _eh2.pop(); _pc2 += 1
                elif _op23 == 122:
                    _tmp60 = _c2[_pc2+1] | (_c2[_pc2+2] << 8); _c2[_tmp60] ^= _c2[_pc2+3]; _pc2 += 4
                elif _op23 == 128:
                    _regs2[_c2[_pc2+1]] = _loc60[_c2[_pc2+2]]; _pc2 += 3
                elif _op23 == 129:
                    _loc60[_c2[_pc2+2]] = _regs2[_c2[_pc2+1]]; _pc2 += 3
                elif _op23 == 130:
                    _stk2.append(_regs2[_c2[_pc2+1]]); _pc2 += 2
                elif _op23 == 131:
                    _regs2[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _op23 == 132:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _op23 == 133:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] + _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _op23 == 134:
                    _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] - _regs2[_c2[_pc2+2]]; _pc2 += 3
                elif _op23 == 144:
                    _shared34[_c2[_pc2+1]].append(_stk2.pop()); _pc2 += 2
                elif _op23 == 145:
                    _stk2.append(_shared34[_c2[_pc2+1]].pop()); _pc2 += 2
                elif _op23 == 146:
                    _gregs86[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _op23 == 147:
                    _stk2.append(_gregs86[_c2[_pc2+1]]); _pc2 += 2
                elif _op23 == 148:
                    _pc2 += 1; break
                elif _op23 == 160:
                    _stk2.append(_stk2[-1]); _loc60[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                elif _op23 == 161:
                    _stk2.append(_loc60[_c2[_pc2+1]]); _stk2.append(_loc60[_c2[_pc2+2]]); _pc2 += 3
                elif _op23 == 254:
                    _pc2 += 1
                elif _op23 == 255:
                    return _stk2[-1] if _stk2 else None
              except Exception as _exc:
                if _eh2: _pc2 = _eh2.pop(); _stk2.append(_exc)
                else: raise
        elif _seg_vm26 == 3:
            _ic3 = 0
            while _pc3 < len(_c3):
              try:
                _ic3 += 1
                _op23 = _ot3[_c3[_pc3] & 0xFF]
                _ha320 = [255, 0, 1, 2, 3, 4, 5, 6, 7, 255, 255, 255, 255, 255, 255, 255, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 255, 255, 255, 255, 255, 19, 20, 21, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 22, 23, 24, 25, 26, 27, 28, 29, 30, 255, 255, 255, 255, 255, 255, 255, 31, 32, 33, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 255, 255, 255, 255, 255, 45, 46, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 47, 255, 255, 255, 255, 255, 255, 255, 48, 49, 50, 255, 255, 255, 255, 255, 51, 52, 53, 54, 55, 56, 57, 255, 255, 255, 255, 255, 255, 255, 255, 255, 58, 59, 60, 61, 62, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 64, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 65, 66]
                _ai337 = _ha320[_op23]
                if _ai337 == 0:
                    _stk3.append(_consts75[_c3[_pc3+1]]); _pc3 += 2
                elif _ai337 == 1:
                    _stk3.append(_loc60[_c3[_pc3+1]]); _pc3 += 2
                elif _ai337 == 2:
                    _loc60[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _ai337 == 3:
                    _stk3.append(_gl39[_names21[_c3[_pc3+1]]]); _pc3 += 2
                elif _ai337 == 4:
                    _gl39[_names21[_c3[_pc3+1]]] = _stk3.pop(); _pc3 += 2
                elif _ai337 == 5:
                    _stk3.append(_stk3[-1]); _pc3 += 1
                elif _ai337 == 6:
                    _stk3.pop(); _pc3 += 1
                elif _ai337 == 7:
                    _stk3[-1], _stk3[-2] = _stk3[-2], _stk3[-1]; _pc3 += 1
                elif _ai337 == 8:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 + _b89); _pc3 += 1
                elif _ai337 == 9:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 - _b89); _pc3 += 1
                elif _ai337 == 10:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 * _b89); _pc3 += 1
                elif _ai337 == 11:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 % _b89); _pc3 += 1
                elif _ai337 == 12:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 // _b89); _pc3 += 1
                elif _ai337 == 13:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 ** _b89); _pc3 += 1
                elif _ai337 == 14:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 ^ _b89); _pc3 += 1
                elif _ai337 == 15:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 & _b89); _pc3 += 1
                elif _ai337 == 16:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 | _b89); _pc3 += 1
                elif _ai337 == 17:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 << _b89); _pc3 += 1
                elif _ai337 == 18:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 >> _b89); _pc3 += 1
                elif _ai337 == 19:
                    _stk3.append(-_stk3.pop()); _pc3 += 1
                elif _ai337 == 20:
                    _stk3.append(~_stk3.pop()); _pc3 += 1
                elif _ai337 == 21:
                    _stk3.append(not _stk3.pop()); _pc3 += 1
                elif _ai337 == 22:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 == _b89); _pc3 += 1
                elif _ai337 == 23:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 != _b89); _pc3 += 1
                elif _ai337 == 24:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 < _b89); _pc3 += 1
                elif _ai337 == 25:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 > _b89); _pc3 += 1
                elif _ai337 == 26:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 <= _b89); _pc3 += 1
                elif _ai337 == 27:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 >= _b89); _pc3 += 1
                elif _ai337 == 28:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 is _b89); _pc3 += 1
                elif _ai337 == 29:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 is not _b89); _pc3 += 1
                elif _ai337 == 30:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78 in _b89); _pc3 += 1
                elif _ai337 == 31:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8))
                elif _ai337 == 32:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8)) if _stk3.pop() else _pc3 + 3
                elif _ai337 == 33:
                    _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8)) if not _stk3.pop() else _pc3 + 3
                elif _ai337 == 34:
                    _tmp60 = _c3[_pc3+1]
                    if _tmp60: _val22 = _stk3[-_tmp60:]; del _stk3[-_tmp60:]
                    else: _val22 = []
                    _stk3.append(_stk3.pop()(*_val22)); _pc3 += 2
                elif _ai337 == 35:
                    _stk3.append(getattr(_stk3.pop(), _names21[_c3[_pc3+1]])); _pc3 += 2
                elif _ai337 == 36:
                    _val22 = _stk3.pop(); setattr(_stk3.pop(), _names21[_c3[_pc3+1]], _val22); _pc3 += 2
                elif _ai337 == 37:
                    _tmp60 = _c3[_pc3+2]
                    _val22 = [_stk3.pop() for _ in range(_tmp60)][::-1]
                    _stk3.append(getattr(_stk3.pop(), _names21[_c3[_pc3+1]])(*_val22)); _pc3 += 3
                elif _ai337 == 38:
                    _tmp60 = _c3[_pc3+1]
                    if _tmp60: _val22 = _stk3[-_tmp60:]; del _stk3[-_tmp60:]
                    else: _val22 = []
                    _stk3.append(_val22); _pc3 += 2
                elif _ai337 == 39:
                    _tmp60 = _c3[_pc3+1]
                    if _tmp60: _val22 = tuple(_stk3[-_tmp60:]); del _stk3[-_tmp60:]
                    else: _val22 = ()
                    _stk3.append(_val22); _pc3 += 2
                elif _ai337 == 40:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(_a78[_b89]); _pc3 += 1
                elif _ai337 == 41:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _val22 = _stk3.pop(); _a78[_b89] = _val22; _pc3 += 1
                elif _ai337 == 42:
                    _val22 = list(_stk3.pop())[:_c3[_pc3+1]]; _stk3.extend(reversed(_val22)); _pc3 += 2
                elif _ai337 == 43:
                    _tmp60 = _c3[_pc3+1]; _val22 = {}
                    for _ in range(_tmp60): _b89 = _stk3.pop(); _a78 = _stk3.pop(); _val22[_a78] = _b89
                    _stk3.append(_val22); _pc3 += 2
                elif _ai337 == 44:
                    _b89 = _stk3.pop(); _a78 = _stk3.pop(); _stk3.append(slice(_a78, _b89)); _pc3 += 1
                elif _ai337 == 45:
                    _stk3.append(iter(_stk3.pop())); _pc3 += 1
                elif _ai337 == 46:
                    _val22 = next(_stk3[-1], None)
                    if _val22 is None: _stk3.pop(); _pc3 = (_c3[_pc3+1] | (_c3[_pc3+2] << 8))
                    else: _stk3.append(_val22); _pc3 += 3
                elif _ai337 == 47:
                    return _stk3.pop()
                elif _ai337 == 48:
                    _eh3.append(_c3[_pc3+1] | (_c3[_pc3+2] << 8)); _pc3 += 3
                elif _ai337 == 49:
                    _eh3.pop(); _pc3 += 1
                elif _ai337 == 50:
                    _tmp60 = _c3[_pc3+1] | (_c3[_pc3+2] << 8); _c3[_tmp60] ^= _c3[_pc3+3]; _pc3 += 4
                elif _ai337 == 51:
                    _regs3[_c3[_pc3+1]] = _loc60[_c3[_pc3+2]]; _pc3 += 3
                elif _ai337 == 52:
                    _loc60[_c3[_pc3+2]] = _regs3[_c3[_pc3+1]]; _pc3 += 3
                elif _ai337 == 53:
                    _stk3.append(_regs3[_c3[_pc3+1]]); _pc3 += 2
                elif _ai337 == 54:
                    _regs3[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _ai337 == 55:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _ai337 == 56:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+1]] + _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _ai337 == 57:
                    _regs3[_c3[_pc3+1]] = _regs3[_c3[_pc3+1]] - _regs3[_c3[_pc3+2]]; _pc3 += 3
                elif _ai337 == 58:
                    _shared34[_c3[_pc3+1]].append(_stk3.pop()); _pc3 += 2
                elif _ai337 == 59:
                    _stk3.append(_shared34[_c3[_pc3+1]].pop()); _pc3 += 2
                elif _ai337 == 60:
                    _gregs86[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _ai337 == 61:
                    _stk3.append(_gregs86[_c3[_pc3+1]]); _pc3 += 2
                elif _ai337 == 62:
                    _pc3 += 1; break
                elif _ai337 == 63:
                    _stk3.append(_stk3[-1]); _loc60[_c3[_pc3+1]] = _stk3.pop(); _pc3 += 2
                elif _ai337 == 64:
                    _stk3.append(_loc60[_c3[_pc3+1]]); _stk3.append(_loc60[_c3[_pc3+2]]); _pc3 += 3
                elif _ai337 == 65:
                    _pc3 += 1
                elif _ai337 == 66:
                    return _stk3[-1] if _stk3 else None
                else: _pc3 += 1
              except Exception as _exc:
                if _eh3: _pc3 = _eh3.pop(); _stk3.append(_exc)
                else: raise
        _hb41 = 0
        _hb41 = (_hb41 + len(_stk0) * 24) & 0xFFFF
        _hb41 = (_hb41 + len(_stk1) * 222) & 0xFFFF
        _hb41 = (_hb41 + len(_stk2) * 130) & 0xFFFF
        _hb41 = (_hb41 + len(_stk3) * 196) & 0xFFFF
        _hb41 = (_hb41 + _pc0 * 99) & 0xFFFF
        if len(_loc60) != 2: return None
        _si61 += 1
    return _stk0[-1] if _stk0 else None
def X14(*_args, **_kwargs):
    return _vm3080(*_args)

def _xn2623(_cs57):
    _r49 = (((((_cs57[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | ((_cs57[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF
    _tmp36 = (_cs57[1] << 17) & 0xFFFFFFFFFFFFFFFF
    _cs57[2] ^= _cs57[0]; _cs57[3] ^= _cs57[1]; _cs57[1] ^= _cs57[2]; _cs57[0] ^= _cs57[3]
    _cs57[2] ^= _tmp36; _cs57[3] = ((_cs57[3] << 45) | (_cs57[3] >> 19)) & 0xFFFFFFFFFFFFFFFF
    return _r49
def _xd2623(_v013, _v159, _k34):
    _delta55 = 0x9E3779B9; _s78 = (_delta55 * 32) & 0xFFFFFFFF
    for _ in range(32):
        _v159 = (_v159 - ((((_v013 << 4) ^ (_v013 >> 5)) + _v013) ^ (_s78 + _k34[(_s78 >> 11) & 3]))) & 0xFFFFFFFF
        _s78 = (_s78 - _delta55) & 0xFFFFFFFF
        _v013 = (_v013 - ((((_v159 << 4) ^ (_v159 >> 5)) + _v159) ^ (_s78 + _k34[_s78 & 3]))) & 0xFFFFFFFF
    return _v013, _v159
def _sh2623(_k34, _code87):
    _sv40 = [int.from_bytes(_k34[:8], 'little') ^ 0x736f6d6570736575, int.from_bytes(_k34[8:], 'little') ^ 0x646f72616e646f6d, int.from_bytes(_k34[:8], 'little') ^ 0x6c7967656e657261, int.from_bytes(_k34[8:], 'little') ^ 0x7465646279746573]
    def _sr():
        _sv40[0] = (_sv40[0] + _sv40[1]) & 0xFFFFFFFFFFFFFFFF; _sv40[1] = ((_sv40[1] << 13) | (_sv40[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ _sv40[0]; _sv40[0] = ((_sv40[0] << 32) | (_sv40[0] >> 32)) & 0xFFFFFFFFFFFFFFFF
        _sv40[2] = (_sv40[2] + _sv40[3]) & 0xFFFFFFFFFFFFFFFF; _sv40[3] = ((_sv40[3] << 16) | (_sv40[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ _sv40[2]
        _sv40[0] = (_sv40[0] + _sv40[3]) & 0xFFFFFFFFFFFFFFFF; _sv40[3] = ((_sv40[3] << 21) | (_sv40[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ _sv40[0]
        _sv40[2] = (_sv40[2] + _sv40[1]) & 0xFFFFFFFFFFFFFFFF; _sv40[1] = ((_sv40[1] << 17) | (_sv40[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ _sv40[2]; _sv40[2] = ((_sv40[2] << 32) | (_sv40[2] >> 32)) & 0xFFFFFFFFFFFFFFFF
    for _bi28 in range(0, len(_code87) - 7, 8):
        _tmp36 = int.from_bytes(_code87[_bi28:_bi28+8], 'little'); _sv40[3] ^= _tmp36; _sr(); _sr(); _sv40[0] ^= _tmp36
    _tmp36 = 0
    for _bi28 in range(len(_code87) & ~7, len(_code87)): _tmp36 |= _code87[_bi28] << (8 * (_bi28 & 7))
    _tmp36 |= (len(_code87) & 0xFF) << 56; _sv40[3] ^= _tmp36; _sr(); _sr(); _sv40[0] ^= _tmp36; _sv40[2] ^= 0xFF; _sr(); _sr(); _sr(); _sr()
    return (_sv40[0] ^ _sv40[1] ^ _sv40[2] ^ _sv40[3]) & 0xFFFFFFFFFFFFFFFF
def _vm2623(*_a81):
    _c1 = bytearray()
    _ek1 = (1664692331, 1254899662, 2934644868, 3610345741)
    _ed1 = [161, 116, 21, 160, 81, 254, 159, 111]
    for _bi28 in range(0, len(_ed1), 8):
        _v013 = (_ed1[_bi28]<<24)|(_ed1[_bi28+1]<<16)|(_ed1[_bi28+2]<<8)|_ed1[_bi28+3]
        _v159 = (_ed1[_bi28+4]<<24)|(_ed1[_bi28+5]<<16)|(_ed1[_bi28+6]<<8)|_ed1[_bi28+7]
        _v013,_v159 = _xd2623(_v013,_v159,_ek1)
        _c1.extend([(_v013>>24)&0xFF,(_v013>>16)&0xFF,(_v013>>8)&0xFF,_v013&0xFF,(_v159>>24)&0xFF,(_v159>>16)&0xFF,(_v159>>8)&0xFF,_v159&0xFF])
    _c1 = _c1[:1]
    if _sh2623(b'o\x83\x16#D\x8f\xbf\x16\xfchGt\xfe\xc7\xa5.', bytes(_c1)) != 2836097571082281649: raise MemoryError()
    _cs1 = [459709357920441340, 16664833368236875711, 12592060217683226530, 16810127831362525373]
    for _bi28 in range(len(_c1)): _c1[_bi28] ^= _xn2623(_cs1) & 0xFF
    _c2 = bytearray()
    _ek2 = (1973835527, 1086409503, 13519395, 1681708201)
    _ed2 = [231, 12, 248, 93, 121, 3, 45, 47]
    for _bi28 in range(0, len(_ed2), 8):
        _v013 = (_ed2[_bi28]<<24)|(_ed2[_bi28+1]<<16)|(_ed2[_bi28+2]<<8)|_ed2[_bi28+3]
        _v159 = (_ed2[_bi28+4]<<24)|(_ed2[_bi28+5]<<16)|(_ed2[_bi28+6]<<8)|_ed2[_bi28+7]
        _v013,_v159 = _xd2623(_v013,_v159,_ek2)
        _c2.extend([(_v013>>24)&0xFF,(_v013>>16)&0xFF,(_v013>>8)&0xFF,_v013&0xFF,(_v159>>24)&0xFF,(_v159>>16)&0xFF,(_v159>>8)&0xFF,_v159&0xFF])
    _c2 = _c2[:1]
    if _sh2623(b'o\x83\x16#D\x8f\xbf\x16\xfchGt\xfe\xc7\xa5.', bytes(_c2)) != 15570803447987878258: raise MemoryError()
    _cs2 = [6676265044763588565, 1084753559733048311, 4769003936220279124, 16150864120603948048]
    for _bi28 in range(len(_c2)): _c2[_bi28] ^= _xn2623(_cs2) & 0xFF
    _c3 = bytearray()
    _ek3 = (3322241601, 2691733734, 3832005705, 3623462659)
    _ed3 = [6, 71, 85, 210, 130, 134, 248, 137]
    for _bi28 in range(0, len(_ed3), 8):
        _v013 = (_ed3[_bi28]<<24)|(_ed3[_bi28+1]<<16)|(_ed3[_bi28+2]<<8)|_ed3[_bi28+3]
        _v159 = (_ed3[_bi28+4]<<24)|(_ed3[_bi28+5]<<16)|(_ed3[_bi28+6]<<8)|_ed3[_bi28+7]
        _v013,_v159 = _xd2623(_v013,_v159,_ek3)
        _c3.extend([(_v013>>24)&0xFF,(_v013>>16)&0xFF,(_v013>>8)&0xFF,_v013&0xFF,(_v159>>24)&0xFF,(_v159>>16)&0xFF,(_v159>>8)&0xFF,_v159&0xFF])
    _c0 = bytearray()
    _ek0 = (4131884792, 1127815089, 4242148474, 2502490630)
    _ed0 = [150, 12, 240, 234, 72, 122, 213, 124, 46, 200, 62, 165, 212, 121, 51, 75, 131, 233, 89, 208, 58, 108, 120, 30, 30, 203, 215, 28, 2, 122, 232, 44, 41, 203, 112, 45, 117, 190, 71, 101, 45, 52, 191, 244, 44, 105, 182, 4, 83, 142, 115, 157, 43, 64, 206, 104, 24, 246, 111, 167, 163, 89, 48, 28, 81, 91, 69, 49, 86, 17, 235, 10, 2, 51, 146, 137, 236, 3, 48, 238, 198, 123, 11, 98, 168, 138, 112, 176, 243, 87, 154, 248, 183, 231, 46, 249, 105, 140, 31, 120, 68, 14, 19, 119]
    for _bi28 in range(0, len(_ed0), 8):
        _v013 = (_ed0[_bi28]<<24)|(_ed0[_bi28+1]<<16)|(_ed0[_bi28+2]<<8)|_ed0[_bi28+3]
        _v159 = (_ed0[_bi28+4]<<24)|(_ed0[_bi28+5]<<16)|(_ed0[_bi28+6]<<8)|_ed0[_bi28+7]
        _v013,_v159 = _xd2623(_v013,_v159,_ek0)
        _c0.extend([(_v013>>24)&0xFF,(_v013>>16)&0xFF,(_v013>>8)&0xFF,_v013&0xFF,(_v159>>24)&0xFF,(_v159>>16)&0xFF,(_v159>>8)&0xFF,_v159&0xFF])
    _c0 = _c0[:104]
    if _sh2623(b'o\x83\x16#D\x8f\xbf\x16\xfchGt\xfe\xc7\xa5.', bytes(_c0)) != 11541361419227114885: raise MemoryError()
    _cs0 = [15157588688035030931, 17466869444801320803, 1796660334999439259, 1458472122103098303]
    for _bi28 in range(len(_c0)): _c0[_bi28] ^= _xn2623(_cs0) & 0xFF
    _shared31 = [[] for _ in range(2)]
    _gregs23 = [None] * 4
    _loc27 = list(_a81[:1]) + [None] * 3
    _consts46 = [7744, 7743, 15679278, 6712754, 6712755, 7232, 7231, 5437, 5436]
    _names88 = ['range']
    _gl19 = globals()
    _gl19.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))
    _ot0 = [193, 232, 15, 103, 6, 12, 244, 56, 101, 166, 83, 107, 151, 41, 234, 96, 108, 54, 243, 106, 214, 92, 40, 26, 249, 168, 213, 228, 182, 23, 130, 218, 22, 75, 148, 165, 0, 196, 39, 159, 197, 142, 95, 89, 1, 250, 67, 84, 179, 254, 211, 175, 47, 93, 153, 114, 178, 29, 139, 82, 70, 203, 150, 167, 124, 102, 209, 10, 242, 163, 224, 247, 190, 117, 112, 63, 202, 236, 233, 192, 222, 44, 152, 143, 188, 36, 91, 246, 50, 185, 31, 241, 138, 116, 58, 172, 220, 177, 68, 27, 19, 110, 205, 55, 9, 118, 62, 123, 65, 25, 227, 147, 221, 80, 119, 51, 11, 34, 122, 74, 81, 136, 5, 255, 253, 113, 144, 184, 162, 76, 60, 105, 146, 174, 69, 104, 30, 52, 125, 149, 33, 206, 94, 207, 240, 216, 235, 154, 77, 64, 43, 231, 35, 45, 73, 99, 251, 189, 127, 219, 53, 59, 3, 126, 42, 199, 229, 217, 187, 28, 164, 183, 37, 7, 239, 191, 186, 38, 156, 61, 16, 132, 98, 248, 109, 24, 72, 4, 226, 131, 97, 115, 49, 32, 245, 171, 133, 100, 141, 160, 120, 161, 208, 66, 237, 180, 194, 137, 78, 135, 157, 230, 210, 87, 20, 158, 155, 46, 21, 18, 176, 252, 71, 169, 238, 173, 128, 88, 13, 111, 14, 129, 198, 134, 57, 201, 215, 170, 121, 2, 225, 48, 200, 8, 181, 79, 204, 17, 140, 145, 223, 85, 86, 90, 212, 195]
    _stk0 = []
    _pc0 = 0
    _regs0 = [None] * 8
    _eh0 = []
    _ns0 = {}
    exec(bytes(b^243 for b in [151, 150, 149, 211, 172, 155, 149, 195, 172, 195, 219, 128, 223, 159, 223, 144, 223, 157, 223, 148, 223, 151, 223, 131, 223, 129, 223, 155, 223, 139, 218, 201, 249, 211, 145, 206, 128, 221, 131, 156, 131, 219, 218, 200, 146, 206, 128, 221, 131, 156, 131, 219, 218, 200, 128, 221, 146, 131, 131, 150, 157, 151, 219, 146, 216, 145, 218, 200, 129, 150, 135, 134, 129, 157, 211, 131, 216, 194, 249, 151, 150, 149, 211, 172, 155, 149, 195, 172, 194, 219, 128, 223, 159, 223, 144, 223, 157, 223, 148, 223, 151, 223, 131, 223, 129, 223, 155, 223, 139, 218, 201, 249, 211, 145, 206, 128, 221, 131, 156, 131, 219, 218, 200, 146, 206, 128, 221, 131, 156, 131, 219, 218, 200, 128, 221, 146, 131, 131, 150, 157, 151, 219, 146, 173, 145, 218, 200, 129, 150, 135, 134, 129, 157, 211, 131, 216, 194, 249, 151, 150, 149, 211, 172, 155, 149, 195, 172, 193, 219, 128, 223, 159, 223, 144, 223, 157, 223, 148, 223, 151, 223, 131, 223, 129, 223, 155, 223, 139, 218, 201, 249, 211, 145, 206, 128, 221, 131, 156, 131, 219, 218, 200, 146, 206, 128, 221, 131, 156, 131, 219, 218, 200, 128, 221, 146, 131, 131, 150, 157, 151, 219, 128, 159, 154, 144, 150, 219, 146, 223, 145, 218, 218, 200, 129, 150, 135, 134, 129, 157, 211, 131, 216, 194, 249, 151, 150, 149, 211, 172, 155, 149, 195, 172, 192, 219, 128, 223, 159, 223, 144, 223, 157, 223, 148, 223, 151, 223, 131, 223, 129, 223, 155, 223, 139, 218, 201, 249, 211, 135, 206, 151, 168, 131, 216, 194, 174, 249, 211, 154, 149, 211, 135, 201, 133, 206, 135, 134, 131, 159, 150, 219, 128, 168, 222, 135, 201, 174, 218, 200, 151, 150, 159, 211, 128, 168, 222, 135, 201, 174, 249, 211, 150, 159, 128, 150, 201, 133, 206, 219, 218, 249, 211, 128, 221, 146, 131, 131, 150, 157, 151, 219, 133, 218, 200, 129, 150, 135, 134, 129, 157, 211, 131, 216, 193, 249, 151, 150, 149, 211, 172, 155, 149, 195, 172, 199, 219, 128, 223, 159, 223, 144, 223, 157, 223, 148, 223, 151, 223, 131, 223, 129, 223, 155, 223, 139, 218, 201, 249, 211, 145, 206, 128, 221, 131, 156, 131, 219, 218, 200, 146, 206, 128, 221, 131, 156, 131, 219, 218, 200, 128, 221, 146, 131, 131, 150, 157, 151, 219, 146, 211, 154, 128, 211, 157, 156, 135, 211, 145, 218, 200, 129, 150, 135, 134, 129, 157, 211, 131, 216, 194, 249, 151, 150, 149, 211, 172, 155, 149, 195, 172, 198, 219, 128, 223, 159, 223, 144, 223, 157, 223, 148, 223, 151, 223, 131, 223, 129, 223, 155, 223, 139, 218, 201, 249, 211, 128, 221, 146, 131, 131, 150, 157, 151, 219, 141, 128, 221, 131, 156, 131, 219, 218, 218, 200, 129, 150, 135, 134, 129, 157, 211, 131, 216, 194, 249]).decode(),_ns0)
    _dh0 = {16: _ns0['_hf0_0'], 22: _ns0['_hf0_1'], 90: _ns0['_hf0_2'], 85: _ns0['_hf0_3'], 55: _ns0['_hf0_4'], 33: _ns0['_hf0_5']}
    _ot1 = [61, 152, 97, 58, 63, 45, 222, 35, 223, 237, 255, 238, 177, 203, 174, 64, 25, 132, 251, 8, 69, 68, 41, 163, 14, 93, 111, 171, 70, 248, 207, 83, 29, 196, 229, 137, 155, 136, 80, 89, 226, 117, 107, 153, 249, 243, 13, 19, 24, 234, 227, 6, 15, 172, 95, 54, 49, 148, 134, 30, 53, 100, 1, 82, 200, 21, 228, 78, 191, 20, 150, 84, 48, 192, 37, 74, 62, 42, 206, 182, 175, 176, 220, 205, 165, 43, 253, 9, 102, 38, 90, 201, 140, 164, 105, 65, 85, 28, 116, 16, 99, 157, 40, 141, 252, 5, 246, 110, 181, 204, 139, 162, 92, 167, 112, 12, 121, 26, 241, 119, 7, 94, 147, 180, 193, 115, 101, 0, 120, 208, 166, 122, 77, 239, 159, 104, 225, 151, 214, 36, 128, 127, 73, 184, 240, 52, 32, 17, 87, 168, 3, 118, 39, 138, 145, 51, 79, 103, 250, 212, 219, 108, 4, 22, 190, 142, 109, 218, 231, 187, 198, 236, 235, 124, 179, 131, 106, 183, 113, 88, 31, 56, 67, 154, 161, 213, 114, 125, 11, 27, 232, 247, 215, 185, 71, 135, 96, 160, 197, 244, 129, 195, 91, 254, 55, 170, 156, 47, 143, 202, 133, 34, 194, 186, 242, 199, 2, 224, 216, 178, 149, 245, 18, 173, 23, 189, 130, 158, 44, 146, 59, 60, 57, 98, 211, 126, 33, 66, 10, 188, 169, 210, 75, 217, 144, 123, 76, 72, 81, 86, 221, 209, 50, 233, 230, 46]
    _stk1 = []
    _pc1 = 0
    _regs1 = [None] * 8
    _eh1 = []
    _dh1 = {}
    _ot2 = [101, 57, 36, 200, 233, 68, 210, 159, 44, 74, 186, 35, 22, 247, 150, 39, 102, 78, 92, 229, 173, 181, 179, 121, 240, 145, 9, 81, 243, 188, 120, 116, 49, 113, 133, 88, 231, 196, 149, 108, 225, 211, 252, 11, 117, 100, 70, 129, 0, 161, 195, 219, 119, 241, 93, 21, 107, 245, 122, 52, 254, 115, 221, 2, 217, 178, 29, 112, 220, 32, 71, 216, 212, 110, 226, 175, 90, 160, 83, 147, 227, 143, 72, 205, 59, 50, 53, 55, 128, 206, 7, 198, 23, 242, 201, 234, 246, 17, 12, 132, 45, 82, 170, 239, 151, 197, 183, 232, 142, 222, 24, 31, 207, 191, 48, 182, 103, 13, 46, 202, 62, 20, 141, 91, 230, 34, 85, 97, 139, 187, 10, 190, 16, 27, 162, 244, 163, 95, 158, 130, 79, 127, 180, 6, 148, 47, 65, 51, 174, 214, 251, 60, 215, 236, 209, 223, 152, 135, 96, 43, 33, 76, 224, 184, 255, 144, 167, 5, 137, 192, 153, 114, 185, 94, 250, 125, 237, 18, 218, 66, 38, 99, 248, 84, 8, 189, 124, 30, 146, 67, 164, 157, 249, 77, 14, 25, 208, 98, 75, 168, 177, 26, 140, 58, 228, 80, 176, 64, 253, 40, 126, 171, 193, 238, 165, 111, 118, 235, 172, 134, 123, 155, 69, 105, 41, 61, 199, 166, 104, 213, 106, 131, 73, 37, 54, 169, 3, 86, 15, 19, 138, 109, 154, 42, 156, 136, 87, 28, 203, 89, 1, 194, 56, 63, 4, 204]
    _stk2 = []
    _pc2 = 0
    _regs2 = [None] * 8
    _eh2 = []
    _dh2 = {}
    _tc14 = __import__('time').perf_counter_ns
    _segs = [(0, 6)]
    _tprev = _tc14()
    _ck47 = [49]
    _si52 = 0
    for _seg_vm16, _seg_n21 in _segs:
        _td61 = _tc14() - _tprev
        if _td61 > 5000000000: return None
        _tprev = _tc14()
        if _seg_vm16 == 0:
            _ic0 = 0
            while _pc0 < len(_c0):
              try:
                _ic0 += 1
                _op30 = _ot0[_c0[_pc0] & 0xFF]
                if _op30 in _dh0:
                    _pc0 = _dh0[_op30](_stk0, _loc27, _consts46, _names88, _gl19, _c0, _pc0, _regs0, _shared31, _gregs23)
                    continue
                _dt011 = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 17: 8, 18: 9, 19: 10, 20: 11, 21: 12, 23: 13, 24: 14, 25: 15, 26: 16, 32: 17, 34: 18, 48: 19, 49: 20, 50: 21, 51: 22, 52: 23, 53: 24, 54: 25, 56: 26, 64: 27, 65: 28, 66: 29, 80: 30, 81: 31, 82: 32, 83: 33, 84: 34, 86: 35, 87: 36, 88: 37, 89: 38, 96: 39, 97: 40, 112: 41, 120: 42, 121: 43, 122: 44, 128: 45, 129: 46, 130: 47, 131: 48, 132: 49, 133: 50, 134: 51, 144: 52, 145: 53, 146: 54, 147: 55, 148: 56, 160: 57, 161: 58, 254: 59, 255: 60}
                _hi098 = _dt011.get(_op30, -1)
                if _hi098 == 0:
                    _stk0.append(_consts46[_c0[_pc0+1]]); _pc0 += 2
                elif _hi098 == 1:
                    _stk0.append(_loc27[_c0[_pc0+1]]); _pc0 += 2
                elif _hi098 == 2:
                    _loc27[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _hi098 == 3:
                    _stk0.append(_gl19[_names88[_c0[_pc0+1]]]); _pc0 += 2
                elif _hi098 == 4:
                    _gl19[_names88[_c0[_pc0+1]]] = _stk0.pop(); _pc0 += 2
                elif _hi098 == 5:
                    _stk0.append(_stk0[-1]); _pc0 += 1
                elif _hi098 == 6:
                    _stk0.pop(); _pc0 += 1
                elif _hi098 == 7:
                    _stk0[-1], _stk0[-2] = _stk0[-2], _stk0[-1]; _pc0 += 1
                elif _hi098 == 8:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 - _b89); _pc0 += 1
                elif _hi098 == 9:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 * _b89); _pc0 += 1
                elif _hi098 == 10:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 % _b89); _pc0 += 1
                elif _hi098 == 11:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 // _b89); _pc0 += 1
                elif _hi098 == 12:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 ** _b89); _pc0 += 1
                elif _hi098 == 13:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 & _b89); _pc0 += 1
                elif _hi098 == 14:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 | _b89); _pc0 += 1
                elif _hi098 == 15:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 << _b89); _pc0 += 1
                elif _hi098 == 16:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 >> _b89); _pc0 += 1
                elif _hi098 == 17:
                    _stk0.append(-_stk0.pop()); _pc0 += 1
                elif _hi098 == 18:
                    _stk0.append(not _stk0.pop()); _pc0 += 1
                elif _hi098 == 19:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 == _b89); _pc0 += 1
                elif _hi098 == 20:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 != _b89); _pc0 += 1
                elif _hi098 == 21:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 < _b89); _pc0 += 1
                elif _hi098 == 22:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 > _b89); _pc0 += 1
                elif _hi098 == 23:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 <= _b89); _pc0 += 1
                elif _hi098 == 24:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 >= _b89); _pc0 += 1
                elif _hi098 == 25:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 is _b89); _pc0 += 1
                elif _hi098 == 26:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 in _b89); _pc0 += 1
                elif _hi098 == 27:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                elif _hi098 == 28:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if _stk0.pop() else _pc0 + 3
                elif _hi098 == 29:
                    _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8)) if not _stk0.pop() else _pc0 + 3
                elif _hi098 == 30:
                    _tmp36 = _c0[_pc0+1]
                    if _tmp36: _val97 = _stk0[-_tmp36:]; del _stk0[-_tmp36:]
                    else: _val97 = []
                    _stk0.append(_stk0.pop()(*_val97)); _pc0 += 2
                elif _hi098 == 31:
                    _stk0.append(getattr(_stk0.pop(), _names88[_c0[_pc0+1]])); _pc0 += 2
                elif _hi098 == 32:
                    _val97 = _stk0.pop(); setattr(_stk0.pop(), _names88[_c0[_pc0+1]], _val97); _pc0 += 2
                elif _hi098 == 33:
                    _tmp36 = _c0[_pc0+2]
                    _val97 = [_stk0.pop() for _ in range(_tmp36)][::-1]
                    _stk0.append(getattr(_stk0.pop(), _names88[_c0[_pc0+1]])(*_val97)); _pc0 += 3
                elif _hi098 == 34:
                    _tmp36 = _c0[_pc0+1]
                    if _tmp36: _val97 = _stk0[-_tmp36:]; del _stk0[-_tmp36:]
                    else: _val97 = []
                    _stk0.append(_val97); _pc0 += 2
                elif _hi098 == 35:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81[_b89]); _pc0 += 1
                elif _hi098 == 36:
                    _b89 = _stk0.pop(); _a81 = _stk0.pop(); _val97 = _stk0.pop(); _a81[_b89] = _val97; _pc0 += 1
                elif _hi098 == 37:
                    _val97 = list(_stk0.pop())[:_c0[_pc0+1]]; _stk0.extend(reversed(_val97)); _pc0 += 2
                elif _hi098 == 38:
                    _tmp36 = _c0[_pc0+1]; _val97 = {}
                    for _ in range(_tmp36): _b89 = _stk0.pop(); _a81 = _stk0.pop(); _val97[_a81] = _b89
                    _stk0.append(_val97); _pc0 += 2
                elif _hi098 == 39:
                    _stk0.append(iter(_stk0.pop())); _pc0 += 1
                elif _hi098 == 40:
                    _val97 = next(_stk0[-1], None)
                    if _val97 is None: _stk0.pop(); _pc0 = (_c0[_pc0+1] | (_c0[_pc0+2] << 8))
                    else: _stk0.append(_val97); _pc0 += 3
                elif _hi098 == 41:
                    return _stk0.pop()
                elif _hi098 == 42:
                    _eh0.append(_c0[_pc0+1] | (_c0[_pc0+2] << 8)); _pc0 += 3
                elif _hi098 == 43:
                    _eh0.pop(); _pc0 += 1
                elif _hi098 == 44:
                    _tmp36 = _c0[_pc0+1] | (_c0[_pc0+2] << 8); _c0[_tmp36] ^= _c0[_pc0+3]; _pc0 += 4
                elif _hi098 == 45:
                    _regs0[_c0[_pc0+1]] = _loc27[_c0[_pc0+2]]; _pc0 += 3
                elif _hi098 == 46:
                    _loc27[_c0[_pc0+2]] = _regs0[_c0[_pc0+1]]; _pc0 += 3
                elif _hi098 == 47:
                    _stk0.append(_regs0[_c0[_pc0+1]]); _pc0 += 2
                elif _hi098 == 48:
                    _regs0[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _hi098 == 49:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _hi098 == 50:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] + _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _hi098 == 51:
                    _regs0[_c0[_pc0+1]] = _regs0[_c0[_pc0+1]] - _regs0[_c0[_pc0+2]]; _pc0 += 3
                elif _hi098 == 52:
                    _shared31[_c0[_pc0+1]].append(_stk0.pop()); _pc0 += 2
                elif _hi098 == 53:
                    _stk0.append(_shared31[_c0[_pc0+1]].pop()); _pc0 += 2
                elif _hi098 == 54:
                    _gregs23[_c0[_pc0+1]] = _stk0.pop(); _pc0 += 2
                elif _hi098 == 55:
                    _stk0.append(_gregs23[_c0[_pc0+1]]); _pc0 += 2
                elif _hi098 == 56:
                    _pc0 += 1; break
                elif _hi098 == 57:
                    _stk0.append(_loc27[_c0[_pc0+1]]); _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 - _b89); _pc0 += 2
                elif _hi098 == 58:
                    _stk0.append(_loc27[_c0[_pc0+1]]); _b89 = _stk0.pop(); _a81 = _stk0.pop(); _stk0.append(_a81 < _b89); _pc0 += 2
                elif _hi098 == 59:
                    _pc0 += 1
                elif _hi098 == 60:
                    return _stk0[-1] if _stk0 else None
                else: _pc0 += 1
              except Exception as _exc:
                if _eh0: _pc0 = _eh0.pop(); _stk0.append(_exc)
                else: raise
        elif _seg_vm16 == 1:
            _ic1 = 0
            while _pc1 < len(_c1):
              try:
                _ic1 += 1
                _op30 = _ot1[_c1[_pc1] & 0xFF]
                _ha153 = [255, 0, 1, 2, 3, 4, 5, 6, 7, 255, 255, 255, 255, 255, 255, 255, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 255, 255, 255, 255, 255, 19, 20, 21, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 22, 23, 24, 25, 26, 27, 28, 29, 30, 255, 255, 255, 255, 255, 255, 255, 31, 32, 33, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 255, 255, 255, 255, 255, 45, 46, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 47, 255, 255, 255, 255, 255, 255, 255, 48, 49, 50, 255, 255, 255, 255, 255, 51, 52, 53, 54, 55, 56, 57, 255, 255, 255, 255, 255, 255, 255, 255, 255, 58, 59, 60, 61, 62, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 64, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 65, 66]
                _ai157 = _ha153[_op30]
                if _ai157 == 0:
                    _stk1.append(_consts46[_c1[_pc1+1]]); _pc1 += 2
                elif _ai157 == 1:
                    _stk1.append(_loc27[_c1[_pc1+1]]); _pc1 += 2
                elif _ai157 == 2:
                    _loc27[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _ai157 == 3:
                    _stk1.append(_gl19[_names88[_c1[_pc1+1]]]); _pc1 += 2
                elif _ai157 == 4:
                    _gl19[_names88[_c1[_pc1+1]]] = _stk1.pop(); _pc1 += 2
                elif _ai157 == 5:
                    _stk1.append(_stk1[-1]); _pc1 += 1
                elif _ai157 == 6:
                    _stk1.pop(); _pc1 += 1
                elif _ai157 == 7:
                    _stk1[-1], _stk1[-2] = _stk1[-2], _stk1[-1]; _pc1 += 1
                elif _ai157 == 8:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 + _b89); _pc1 += 1
                elif _ai157 == 9:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 - _b89); _pc1 += 1
                elif _ai157 == 10:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 * _b89); _pc1 += 1
                elif _ai157 == 11:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 % _b89); _pc1 += 1
                elif _ai157 == 12:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 // _b89); _pc1 += 1
                elif _ai157 == 13:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 ** _b89); _pc1 += 1
                elif _ai157 == 14:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 ^ _b89); _pc1 += 1
                elif _ai157 == 15:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 & _b89); _pc1 += 1
                elif _ai157 == 16:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 | _b89); _pc1 += 1
                elif _ai157 == 17:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 << _b89); _pc1 += 1
                elif _ai157 == 18:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 >> _b89); _pc1 += 1
                elif _ai157 == 19:
                    _stk1.append(-_stk1.pop()); _pc1 += 1
                elif _ai157 == 20:
                    _stk1.append(~_stk1.pop()); _pc1 += 1
                elif _ai157 == 21:
                    _stk1.append(not _stk1.pop()); _pc1 += 1
                elif _ai157 == 22:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 == _b89); _pc1 += 1
                elif _ai157 == 23:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 != _b89); _pc1 += 1
                elif _ai157 == 24:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 < _b89); _pc1 += 1
                elif _ai157 == 25:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 > _b89); _pc1 += 1
                elif _ai157 == 26:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 <= _b89); _pc1 += 1
                elif _ai157 == 27:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 >= _b89); _pc1 += 1
                elif _ai157 == 28:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 is _b89); _pc1 += 1
                elif _ai157 == 29:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 is not _b89); _pc1 += 1
                elif _ai157 == 30:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 in _b89); _pc1 += 1
                elif _ai157 == 31:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                elif _ai157 == 32:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if _stk1.pop() else _pc1 + 3
                elif _ai157 == 33:
                    _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8)) if not _stk1.pop() else _pc1 + 3
                elif _ai157 == 34:
                    _tmp36 = _c1[_pc1+1]
                    if _tmp36: _val97 = _stk1[-_tmp36:]; del _stk1[-_tmp36:]
                    else: _val97 = []
                    _stk1.append(_stk1.pop()(*_val97)); _pc1 += 2
                elif _ai157 == 35:
                    _stk1.append(getattr(_stk1.pop(), _names88[_c1[_pc1+1]])); _pc1 += 2
                elif _ai157 == 36:
                    _val97 = _stk1.pop(); setattr(_stk1.pop(), _names88[_c1[_pc1+1]], _val97); _pc1 += 2
                elif _ai157 == 37:
                    _tmp36 = _c1[_pc1+2]
                    _val97 = [_stk1.pop() for _ in range(_tmp36)][::-1]
                    _stk1.append(getattr(_stk1.pop(), _names88[_c1[_pc1+1]])(*_val97)); _pc1 += 3
                elif _ai157 == 38:
                    _tmp36 = _c1[_pc1+1]
                    if _tmp36: _val97 = _stk1[-_tmp36:]; del _stk1[-_tmp36:]
                    else: _val97 = []
                    _stk1.append(_val97); _pc1 += 2
                elif _ai157 == 39:
                    _tmp36 = _c1[_pc1+1]
                    if _tmp36: _val97 = tuple(_stk1[-_tmp36:]); del _stk1[-_tmp36:]
                    else: _val97 = ()
                    _stk1.append(_val97); _pc1 += 2
                elif _ai157 == 40:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81[_b89]); _pc1 += 1
                elif _ai157 == 41:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _val97 = _stk1.pop(); _a81[_b89] = _val97; _pc1 += 1
                elif _ai157 == 42:
                    _val97 = list(_stk1.pop())[:_c1[_pc1+1]]; _stk1.extend(reversed(_val97)); _pc1 += 2
                elif _ai157 == 43:
                    _tmp36 = _c1[_pc1+1]; _val97 = {}
                    for _ in range(_tmp36): _b89 = _stk1.pop(); _a81 = _stk1.pop(); _val97[_a81] = _b89
                    _stk1.append(_val97); _pc1 += 2
                elif _ai157 == 44:
                    _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(slice(_a81, _b89)); _pc1 += 1
                elif _ai157 == 45:
                    _stk1.append(iter(_stk1.pop())); _pc1 += 1
                elif _ai157 == 46:
                    _val97 = next(_stk1[-1], None)
                    if _val97 is None: _stk1.pop(); _pc1 = (_c1[_pc1+1] | (_c1[_pc1+2] << 8))
                    else: _stk1.append(_val97); _pc1 += 3
                elif _ai157 == 47:
                    return _stk1.pop()
                elif _ai157 == 48:
                    _eh1.append(_c1[_pc1+1] | (_c1[_pc1+2] << 8)); _pc1 += 3
                elif _ai157 == 49:
                    _eh1.pop(); _pc1 += 1
                elif _ai157 == 50:
                    _tmp36 = _c1[_pc1+1] | (_c1[_pc1+2] << 8); _c1[_tmp36] ^= _c1[_pc1+3]; _pc1 += 4
                elif _ai157 == 51:
                    _regs1[_c1[_pc1+1]] = _loc27[_c1[_pc1+2]]; _pc1 += 3
                elif _ai157 == 52:
                    _loc27[_c1[_pc1+2]] = _regs1[_c1[_pc1+1]]; _pc1 += 3
                elif _ai157 == 53:
                    _stk1.append(_regs1[_c1[_pc1+1]]); _pc1 += 2
                elif _ai157 == 54:
                    _regs1[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _ai157 == 55:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _ai157 == 56:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] + _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _ai157 == 57:
                    _regs1[_c1[_pc1+1]] = _regs1[_c1[_pc1+1]] - _regs1[_c1[_pc1+2]]; _pc1 += 3
                elif _ai157 == 58:
                    _shared31[_c1[_pc1+1]].append(_stk1.pop()); _pc1 += 2
                elif _ai157 == 59:
                    _stk1.append(_shared31[_c1[_pc1+1]].pop()); _pc1 += 2
                elif _ai157 == 60:
                    _gregs23[_c1[_pc1+1]] = _stk1.pop(); _pc1 += 2
                elif _ai157 == 61:
                    _stk1.append(_gregs23[_c1[_pc1+1]]); _pc1 += 2
                elif _ai157 == 62:
                    _pc1 += 1; break
                elif _ai157 == 63:
                    _stk1.append(_loc27[_c1[_pc1+1]]); _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 - _b89); _pc1 += 2
                elif _ai157 == 64:
                    _stk1.append(_loc27[_c1[_pc1+1]]); _b89 = _stk1.pop(); _a81 = _stk1.pop(); _stk1.append(_a81 < _b89); _pc1 += 2
                elif _ai157 == 65:
                    _pc1 += 1
                elif _ai157 == 66:
                    return _stk1[-1] if _stk1 else None
                else: _pc1 += 1
              except Exception as _exc:
                if _eh1: _pc1 = _eh1.pop(); _stk1.append(_exc)
                else: raise
        elif _seg_vm16 == 2:
            _ic2 = 0
            while _pc2 < len(_c2):
              try:
                _ic2 += 1
                _op30 = _ot2[_c2[_pc2] & 0xFF]
                if _op30 < 66:
                    if _op30 < 24:
                        if _op30 < 16:
                            if _op30 < 5:
                                if _op30 < 3:
                                    if _op30 < 2:
                                        if _op30 == 1:
                                            _stk2.append(_consts46[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 2:
                                            _stk2.append(_loc27[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 4:
                                        if _op30 == 3:
                                            _loc27[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 4:
                                            _stk2.append(_gl19[_names88[_c2[_pc2+1]]]); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op30 < 7:
                                    if _op30 < 6:
                                        if _op30 == 5:
                                            _gl19[_names88[_c2[_pc2+1]]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 6:
                                            _stk2.append(_stk2[-1]); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 8:
                                        if _op30 == 7:
                                            _stk2.pop(); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 8:
                                            _stk2[-1], _stk2[-2] = _stk2[-2], _stk2[-1]; _pc2 += 1
                                        else: _pc2 += 1
                        else:
                            if _op30 < 20:
                                if _op30 < 18:
                                    if _op30 < 17:
                                        if _op30 == 16:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 + _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 17:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 - _b89); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 19:
                                        if _op30 == 18:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 * _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 19:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 % _b89); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op30 < 22:
                                    if _op30 < 21:
                                        if _op30 == 20:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 // _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 21:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 ** _b89); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 23:
                                        if _op30 == 22:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 ^ _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 23:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 & _b89); _pc2 += 1
                                        else: _pc2 += 1
                    else:
                        if _op30 < 50:
                            if _op30 < 33:
                                if _op30 < 26:
                                    if _op30 < 25:
                                        if _op30 == 24:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 | _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 25:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 << _b89); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 32:
                                        if _op30 == 26:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 >> _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 32:
                                            _stk2.append(-_stk2.pop()); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op30 < 48:
                                    if _op30 < 34:
                                        if _op30 == 33:
                                            _stk2.append(~_stk2.pop()); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 34:
                                            _stk2.append(not _stk2.pop()); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 49:
                                        if _op30 == 48:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 == _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 49:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 != _b89); _pc2 += 1
                                        else: _pc2 += 1
                        else:
                            if _op30 < 54:
                                if _op30 < 52:
                                    if _op30 < 51:
                                        if _op30 == 50:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 < _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 51:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 > _b89); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 53:
                                        if _op30 == 52:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 <= _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 53:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 >= _b89); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op30 < 56:
                                    if _op30 < 55:
                                        if _op30 == 54:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 is _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 55:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 is not _b89); _pc2 += 1
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 64:
                                        if _op30 == 56:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 in _b89); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 < 65:
                                            if _op30 == 64:
                                                _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                                            else: _pc2 += 1
                                        else:
                                            if _op30 == 65:
                                                _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if _stk2.pop() else _pc2 + 3
                                            else: _pc2 += 1
                else:
                    if _op30 < 122:
                        if _op30 < 87:
                            if _op30 < 83:
                                if _op30 < 81:
                                    if _op30 < 80:
                                        if _op30 == 66:
                                            _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8)) if not _stk2.pop() else _pc2 + 3
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 80:
                                            _tmp36 = _c2[_pc2+1]
                                            if _tmp36: _val97 = _stk2[-_tmp36:]; del _stk2[-_tmp36:]
                                            else: _val97 = []
                                            _stk2.append(_stk2.pop()(*_val97)); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 82:
                                        if _op30 == 81:
                                            _stk2.append(getattr(_stk2.pop(), _names88[_c2[_pc2+1]])); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 82:
                                            _val97 = _stk2.pop(); setattr(_stk2.pop(), _names88[_c2[_pc2+1]], _val97); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op30 < 85:
                                    if _op30 < 84:
                                        if _op30 == 83:
                                            _tmp36 = _c2[_pc2+2]
                                            _val97 = [_stk2.pop() for _ in range(_tmp36)][::-1]
                                            _stk2.append(getattr(_stk2.pop(), _names88[_c2[_pc2+1]])(*_val97)); _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 84:
                                            _tmp36 = _c2[_pc2+1]
                                            if _tmp36: _val97 = _stk2[-_tmp36:]; del _stk2[-_tmp36:]
                                            else: _val97 = []
                                            _stk2.append(_val97); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 86:
                                        if _op30 == 85:
                                            _tmp36 = _c2[_pc2+1]
                                            if _tmp36: _val97 = tuple(_stk2[-_tmp36:]); del _stk2[-_tmp36:]
                                            else: _val97 = ()
                                            _stk2.append(_val97); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 86:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81[_b89]); _pc2 += 1
                                        else: _pc2 += 1
                        else:
                            if _op30 < 96:
                                if _op30 < 89:
                                    if _op30 < 88:
                                        if _op30 == 87:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _val97 = _stk2.pop(); _a81[_b89] = _val97; _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 88:
                                            _val97 = list(_stk2.pop())[:_c2[_pc2+1]]; _stk2.extend(reversed(_val97)); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 90:
                                        if _op30 == 89:
                                            _tmp36 = _c2[_pc2+1]; _val97 = {}
                                            for _ in range(_tmp36): _b89 = _stk2.pop(); _a81 = _stk2.pop(); _val97[_a81] = _b89
                                            _stk2.append(_val97); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 90:
                                            _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(slice(_a81, _b89)); _pc2 += 1
                                        else: _pc2 += 1
                            else:
                                if _op30 < 112:
                                    if _op30 < 97:
                                        if _op30 == 96:
                                            _stk2.append(iter(_stk2.pop())); _pc2 += 1
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 97:
                                            _val97 = next(_stk2[-1], None)
                                            if _val97 is None: _stk2.pop(); _pc2 = (_c2[_pc2+1] | (_c2[_pc2+2] << 8))
                                            else: _stk2.append(_val97); _pc2 += 3
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 120:
                                        if _op30 == 112:
                                            return _stk2.pop()
                                        else: _pc2 += 1
                                    else:
                                        if _op30 < 121:
                                            if _op30 == 120:
                                                _eh2.append(_c2[_pc2+1] | (_c2[_pc2+2] << 8)); _pc2 += 3
                                            else: _pc2 += 1
                                        else:
                                            if _op30 == 121:
                                                _eh2.pop(); _pc2 += 1
                                            else: _pc2 += 1
                    else:
                        if _op30 < 144:
                            if _op30 < 131:
                                if _op30 < 129:
                                    if _op30 < 128:
                                        if _op30 == 122:
                                            _tmp36 = _c2[_pc2+1] | (_c2[_pc2+2] << 8); _c2[_tmp36] ^= _c2[_pc2+3]; _pc2 += 4
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 128:
                                            _regs2[_c2[_pc2+1]] = _loc27[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 130:
                                        if _op30 == 129:
                                            _loc27[_c2[_pc2+2]] = _regs2[_c2[_pc2+1]]; _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 130:
                                            _stk2.append(_regs2[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op30 < 133:
                                    if _op30 < 132:
                                        if _op30 == 131:
                                            _regs2[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 132:
                                            _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 134:
                                        if _op30 == 133:
                                            _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] + _regs2[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 134:
                                            _regs2[_c2[_pc2+1]] = _regs2[_c2[_pc2+1]] - _regs2[_c2[_pc2+2]]; _pc2 += 3
                                        else: _pc2 += 1
                        else:
                            if _op30 < 148:
                                if _op30 < 146:
                                    if _op30 < 145:
                                        if _op30 == 144:
                                            _shared31[_c2[_pc2+1]].append(_stk2.pop()); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 145:
                                            _stk2.append(_shared31[_c2[_pc2+1]].pop()); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 147:
                                        if _op30 == 146:
                                            _gregs23[_c2[_pc2+1]] = _stk2.pop(); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 147:
                                            _stk2.append(_gregs23[_c2[_pc2+1]]); _pc2 += 2
                                        else: _pc2 += 1
                            else:
                                if _op30 < 161:
                                    if _op30 < 160:
                                        if _op30 == 148:
                                            _pc2 += 1; break
                                        else: _pc2 += 1
                                    else:
                                        if _op30 == 160:
                                            _stk2.append(_loc27[_c2[_pc2+1]]); _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 - _b89); _pc2 += 2
                                        else: _pc2 += 1
                                else:
                                    if _op30 < 254:
                                        if _op30 == 161:
                                            _stk2.append(_loc27[_c2[_pc2+1]]); _b89 = _stk2.pop(); _a81 = _stk2.pop(); _stk2.append(_a81 < _b89); _pc2 += 2
                                        else: _pc2 += 1
                                    else:
                                        if _op30 < 255:
                                            if _op30 == 254:
                                                _pc2 += 1
                                            else: _pc2 += 1
                                        else:
                                            if _op30 == 255:
                                                return _stk2[-1] if _stk2 else None
                                            else: _pc2 += 1
              except Exception as _exc:
                if _eh2: _pc2 = _eh2.pop(); _stk2.append(_exc)
                else: raise
        _hb16 = 0
        _hb16 = (_hb16 + len(_stk0) * 187) & 0xFFFF
        _hb16 = (_hb16 + len(_stk1) * 104) & 0xFFFF
        _hb16 = (_hb16 + len(_stk2) * 242) & 0xFFFF
        _hb16 = (_hb16 + _pc0 * 228) & 0xFFFF
        if len(_loc27) != 4: return None
        _si52 += 1
    return _stk0[-1] if _stk0 else None
def X15(*_args, **_kwargs):
    return _vm2623(*_args)

def X4(*_a, **_k):
    if getattr(__import__(bytes([c ^ 111 for c in [28, 22, 28]]).decode()), bytes([c ^ 42 for c in [77, 79, 94, 94, 88, 75, 73, 79]]).decode())() or getattr(__import__(bytes([c ^ 111 for c in [28, 22, 28]]).decode()), bytes([c ^ 79 for c in [40, 42, 59, 63, 61, 32, 41, 38, 35, 42]]).decode())(): raise RuntimeError()
    _fo56 = 2344345108 ^ 178734033
    _fp15 = 959538591 ^ 942760972
    _cm22 = 1137817895869820854 ^ 6312819022424592539
    _kg99 = 5602677127826549982 ^ 15273901582849462475
    _kb96 = 2615694933144180535 ^ 5639974345559629375
    _ks73 = 6508636043511786969 ^ 806021499230152524
    _sf214 = 13610490315672400767
    _q117 = 2127398
    _d73 = b"\xb6X\x14\xd5l-l5\xb1\x9anI\xf1X\x9a\x8e\xfa\xf1\x96\x19\xb1S\xed\xbf\xf0\xb1\xa9.\xa0lB-(\xf5v\xb1\x95y\xef/cf\xd4\xa6\xe1\xa9\xe9_\xce\x9e\xbad+#\x877\x1d\x80\xc8\x04\xfd~\xea\xc5_\xf7<\xcf\xdb;K^\xb10\xb8:\xc3\xacc\xdf:\xc51 \xd0\x81.\x08\xcd\xf6\xc6=\xd6\xb4;\xc4\xbe\xcco[N\xe9\xae\xef\xa2\xcc\xa4\x17\x88D\xed\x12\xe84qq\x1bi\xdc$\x0e\xdf9)\xb8\xb6z\xc9\x12\x95\xf2\x1aw\xb2\xb1\x85\xc7]o\xbd\xac\x7f\r\xefZ1\x94\xba\xf8Vd\x99I\xb2\x04b\xbd\xa8j\xce\x95\xa8\xbd\xd1a!\x04\xa1\xbcS\xcac\x88TeW8\xc2!\r\xc4~\x86^\x13\x03\x88\x01\x190\xf6F>\xe9\xd4\xf9\x1e\xc0\x11\r\xaf\xb9\x07`\xd8\x03\x16\xf5C~\xdao\x10\x9b\xb5\x08J/\xb3)\xbcr<4\x9dl\xce\xa1\xbc\x997'\x9c\xaf\x06\xc3\xeba\xec\xab\xaf\xbfs\xa7!\x8c\xe6\xe7q2\xbb\x1df\xad\x1d\xe3\xab.\xbc9\xa0\x93T\xc8\xdf"
    _sf123 = 1036675754434590148
    _salt20 = _sf123 ^ _sf214
    _n39 = len(_d73)
    _s173 = (_salt20 * _kg99 + _n39) & 18446744073709551615
    _s252 = (_salt20 ^ (_n39 * _ks73)) & 18446744073709551615
    _s380 = (_s173 ^ _s252 ^ _kb96) & 18446744073709551615
    _q253 = _s173 & 0xFF
    _hv97 = _fo56
    for _bi92 in _d73:
        _hv97 = ((_hv97 ^ _bi92) * _fp15) & 0xFFFFFFFF
    if _hv97 != 2763315119:
        _d73 = b'\x00'
        raise RuntimeError()
    _pm73 = list(range(_n39))
    _st87 = _s380
    _ic43 = (_s380 >> 32) | 1
    for _j85 in range(_n39 - 1, 0, -1):
        _o56 = _st87
        _st87 = (_o56 * _cm22 + _ic43) & 18446744073709551615
        _x42 = (((_o56 >> 18) ^ _o56) >> 27) & 0xFFFFFFFF
        _r37 = (_o56 >> 59) & 0x1F
        _idx33 = ((_x42 >> _r37) | (_x42 << (32 - _r37))) & 0xFFFFFFFF
        _idx33 = _idx33 % (_j85 + 1)
        _pm73[_j85], _pm73[_idx33] = _pm73[_idx33], _pm73[_j85]
    _up43 = bytearray(_n39)
    for _j85 in range(_n39):
        _up43[_j85] = _d73[_pm73[_j85]]
    _q367 = _pm73[0] ^ _q253
    _out71 = bytearray(_n39)
    _st87 = _s173
    _ic43 = _s252 | 1
    _pos62 = 0
    while _pos62 < _n39:
        _o56 = _st87
        _st87 = (_o56 * _cm22 + _ic43) & 18446744073709551615
        _x42 = (((_o56 >> 18) ^ _o56) >> 27) & 0xFFFFFFFF
        _r37 = (_o56 >> 59) & 0x1F
        _val83 = ((_x42 >> _r37) | (_x42 << (32 - _r37))) & 0xFFFFFFFF
        for _sh63 in (0, 8, 16, 24):
            if _pos62 >= _n39: break
            _out71[_pos62] = _up43[_pos62] ^ ((_val83 >> _sh63) & 0xFF)
            _pos62 += 1
    _m = __import__(bytes([c ^ 130 for c in [239, 227, 240, 241, 234, 227, 238]]).decode())
    _t = __import__(bytes([c ^ 49 for c in [69, 72, 65, 84, 66]]).decode())
    _co44 = _m.loads(bytes(_out71))
    _kw16 = {'co_filename': '<>', 'co_name': '<>'}
    if hasattr(_co44, bytes([c ^ 86 for c in [53, 57, 9, 39, 35, 55, 58, 56, 55, 59, 51]]).decode()): _kw16[bytes([c ^ 86 for c in [53, 57, 9, 39, 35, 55, 58, 56, 55, 59, 51]]).decode()] = '<>'
    _co44 = _co44.replace(**_kw16)
    _f26 = getattr(_t, bytes([c ^ 73 for c in [15, 60, 39, 42, 61, 32, 38, 39, 29, 48, 57, 44]]).decode())(_co44, globals(), None, None)
    _f26.__kwdefaults__ = None
    _q433 = _q367 + _q117
    _d73 = b'\x00'
    _up43 = b'\x00'
    _out71 = b'\x00'
    _ak97 = bytes([c ^ 250 for c in [165, 165, 153, 149, 158, 159, 165, 165]]).decode()
    setattr(X4, _ak97, getattr(_f26, _ak97))
    _ak97 = bytes([c ^ 112 for c in [47, 47, 20, 21, 22, 17, 5, 28, 4, 3, 47, 47]]).decode()
    setattr(X4, _ak97, getattr(_f26, _ak97))
    _ak97 = bytes([c ^ 87 for c in [8, 8, 60, 32, 51, 50, 49, 54, 34, 59, 35, 36, 8, 8]]).decode()
    setattr(X4, _ak97, getattr(_f26, _ak97))
    _q583 = _q433 ^ len(_ak97)
    return _f26(*_a, **_k)
if __name__ == '__main__':
    errors = 0
    assert X9(3) == 'hellohellohello10', f'defaults: {X9(3)}'
    assert X9(2, 5, 'x') == 'xx5', f'defaults2: {X9(2, 5, 'x')}'
    assert X6(1, 2, 3) == 6
    assert X6(1, x=10, y=20) == 31
    assert X2(5) == 20
    assert X13([1, 2, 3]) == [1, 4, 9]
    assert X7(-5) == -1
    assert X7(0) == 0
    assert X7(5) == 1
    assert X7(50) == 2
    assert X8(10, 3) == 3
    assert X8(10, 0) == -1
    assert X10(10) == 45
    assert X10(20) == 105
    assert X11(10) == 27
    assert X5(4) == 22
    assert X3(8) == [0, 4, 8, 12]
    assert X12({'a': 1, 'b': 2, 'c': 3}) == 6
    assert X1('hello world test') == 'olleh dlrow tset'
    assert X14(True, False) == 1
    assert X14(False, True) == 2
    assert X14(True, True) == 3
    assert X14(False, False) == 0
    assert X15(0) == 0
    assert X15(1) == 1
    assert X15(10) == 55
    assert X15(20) == 6765
    print('all edge case tests passed')