# Copyright 2017 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "SHORT_EXTERNAL_STRING_TYPE",
  106: "SHORT_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_DOUBLE_ARRAY_TYPE",
  149: "FILLER_TYPE",
  150: "ACCESS_CHECK_INFO_TYPE",
  151: "ACCESSOR_INFO_TYPE",
  152: "ACCESSOR_PAIR_TYPE",
  153: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  154: "ALLOCATION_MEMENTO_TYPE",
  155: "ALLOCATION_SITE_TYPE",
  156: "ASYNC_GENERATOR_REQUEST_TYPE",
  157: "CONTEXT_EXTENSION_TYPE",
  158: "DEBUG_INFO_TYPE",
  159: "FUNCTION_TEMPLATE_INFO_TYPE",
  160: "INTERCEPTOR_INFO_TYPE",
  161: "MODULE_INFO_ENTRY_TYPE",
  162: "MODULE_TYPE",
  163: "OBJECT_TEMPLATE_INFO_TYPE",
  164: "PROMISE_REACTION_JOB_INFO_TYPE",
  165: "PROMISE_RESOLVE_THENABLE_JOB_INFO_TYPE",
  166: "PROTOTYPE_INFO_TYPE",
  167: "SCRIPT_TYPE",
  168: "STACK_FRAME_INFO_TYPE",
  169: "TUPLE2_TYPE",
  170: "TUPLE3_TYPE",
  171: "FIXED_ARRAY_TYPE",
  172: "DESCRIPTOR_ARRAY_TYPE",
  173: "HASH_TABLE_TYPE",
  174: "TRANSITION_ARRAY_TYPE",
  175: "CELL_TYPE",
  176: "CODE_DATA_CONTAINER_TYPE",
  177: "FEEDBACK_VECTOR_TYPE",
  178: "LOAD_HANDLER_TYPE",
  179: "PROPERTY_ARRAY_TYPE",
  180: "PROPERTY_CELL_TYPE",
  181: "SHARED_FUNCTION_INFO_TYPE",
  182: "SMALL_ORDERED_HASH_MAP_TYPE",
  183: "SMALL_ORDERED_HASH_SET_TYPE",
  184: "STORE_HANDLER_TYPE",
  185: "WEAK_CELL_TYPE",
  32768: "JS_PROXY_TYPE",
  32769: "JS_GLOBAL_OBJECT_TYPE",
  32770: "JS_GLOBAL_PROXY_TYPE",
  32771: "JS_MODULE_NAMESPACE_TYPE",
  33024: "JS_SPECIAL_API_OBJECT_TYPE",
  33025: "JS_VALUE_TYPE",
  33280: "JS_API_OBJECT_TYPE",
  33281: "JS_OBJECT_TYPE",
  33282: "JS_ARGUMENTS_TYPE",
  33283: "JS_ARRAY_BUFFER_TYPE",
  33284: "JS_ARRAY_TYPE",
  33285: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  33286: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  33287: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  33288: "JS_DATE_TYPE",
  33289: "JS_ERROR_TYPE",
  33290: "JS_GENERATOR_OBJECT_TYPE",
  33291: "JS_MAP_TYPE",
  33292: "JS_MAP_KEY_ITERATOR_TYPE",
  33293: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  33294: "JS_MAP_VALUE_ITERATOR_TYPE",
  33295: "JS_MESSAGE_OBJECT_TYPE",
  33296: "JS_PROMISE_TYPE",
  33297: "JS_REGEXP_TYPE",
  33298: "JS_SET_TYPE",
  33299: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  33300: "JS_SET_VALUE_ITERATOR_TYPE",
  33301: "JS_STRING_ITERATOR_TYPE",
  33302: "JS_WEAK_MAP_TYPE",
  33303: "JS_WEAK_SET_TYPE",
  33304: "JS_TYPED_ARRAY_TYPE",
  33305: "JS_DATA_VIEW_TYPE",
  33306: "JS_TYPED_ARRAY_KEY_ITERATOR_TYPE",
  33307: "JS_FAST_ARRAY_KEY_ITERATOR_TYPE",
  33308: "JS_GENERIC_ARRAY_KEY_ITERATOR_TYPE",
  33309: "JS_UINT8_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33310: "JS_INT8_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33311: "JS_UINT16_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33312: "JS_INT16_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33313: "JS_UINT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33314: "JS_INT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33315: "JS_FLOAT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33316: "JS_FLOAT64_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33317: "JS_UINT8_CLAMPED_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33318: "JS_FAST_SMI_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33319: "JS_FAST_HOLEY_SMI_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33320: "JS_FAST_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33321: "JS_FAST_HOLEY_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33322: "JS_FAST_DOUBLE_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33323: "JS_FAST_HOLEY_DOUBLE_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33324: "JS_GENERIC_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  33325: "JS_UINT8_ARRAY_VALUE_ITERATOR_TYPE",
  33326: "JS_INT8_ARRAY_VALUE_ITERATOR_TYPE",
  33327: "JS_UINT16_ARRAY_VALUE_ITERATOR_TYPE",
  33328: "JS_INT16_ARRAY_VALUE_ITERATOR_TYPE",
  33329: "JS_UINT32_ARRAY_VALUE_ITERATOR_TYPE",
  33330: "JS_INT32_ARRAY_VALUE_ITERATOR_TYPE",
  33331: "JS_FLOAT32_ARRAY_VALUE_ITERATOR_TYPE",
  33332: "JS_FLOAT64_ARRAY_VALUE_ITERATOR_TYPE",
  33333: "JS_UINT8_CLAMPED_ARRAY_VALUE_ITERATOR_TYPE",
  33334: "JS_FAST_SMI_ARRAY_VALUE_ITERATOR_TYPE",
  33335: "JS_FAST_HOLEY_SMI_ARRAY_VALUE_ITERATOR_TYPE",
  33336: "JS_FAST_ARRAY_VALUE_ITERATOR_TYPE",
  33337: "JS_FAST_HOLEY_ARRAY_VALUE_ITERATOR_TYPE",
  33338: "JS_FAST_DOUBLE_ARRAY_VALUE_ITERATOR_TYPE",
  33339: "JS_FAST_HOLEY_DOUBLE_ARRAY_VALUE_ITERATOR_TYPE",
  33340: "JS_GENERIC_ARRAY_VALUE_ITERATOR_TYPE",
  33341: "WASM_INSTANCE_TYPE",
  33342: "WASM_MEMORY_TYPE",
  33343: "WASM_MODULE_TYPE",
  33344: "WASM_TABLE_TYPE",
  33345: "JS_BOUND_FUNCTION_TYPE",
  33346: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  0x02201: (138, "FreeSpaceMap"),
  0x02251: (132, "MetaMap"),
  0x022a1: (131, "NullMap"),
  0x022f1: (172, "DescriptorArrayMap"),
  0x02341: (171, "FixedArrayMap"),
  0x02391: (149, "OnePointerFillerMap"),
  0x023e1: (149, "TwoPointerFillerMap"),
  0x02431: (131, "UninitializedMap"),
  0x02481: (8, "OneByteInternalizedStringMap"),
  0x024d1: (131, "UndefinedMap"),
  0x02521: (129, "HeapNumberMap"),
  0x02571: (131, "TheHoleMap"),
  0x025c1: (131, "BooleanMap"),
  0x02611: (136, "ByteArrayMap"),
  0x02661: (171, "FixedCOWArrayMap"),
  0x026b1: (173, "HashTableMap"),
  0x02701: (128, "SymbolMap"),
  0x02751: (72, "OneByteStringMap"),
  0x027a1: (171, "ScopeInfoMap"),
  0x027f1: (181, "SharedFunctionInfoMap"),
  0x02841: (133, "CodeMap"),
  0x02891: (171, "FunctionContextMap"),
  0x028e1: (175, "CellMap"),
  0x02931: (185, "WeakCellMap"),
  0x02981: (180, "GlobalPropertyCellMap"),
  0x029d1: (135, "ForeignMap"),
  0x02a21: (174, "TransitionArrayMap"),
  0x02a71: (177, "FeedbackVectorMap"),
  0x02ac1: (131, "ArgumentsMarkerMap"),
  0x02b11: (131, "ExceptionMap"),
  0x02b61: (131, "TerminationExceptionMap"),
  0x02bb1: (131, "OptimizedOutMap"),
  0x02c01: (131, "StaleRegisterMap"),
  0x02c51: (171, "NativeContextMap"),
  0x02ca1: (171, "ModuleContextMap"),
  0x02cf1: (171, "EvalContextMap"),
  0x02d41: (171, "ScriptContextMap"),
  0x02d91: (171, "BlockContextMap"),
  0x02de1: (171, "CatchContextMap"),
  0x02e31: (171, "WithContextMap"),
  0x02e81: (171, "DebugEvaluateContextMap"),
  0x02ed1: (171, "ScriptContextTableMap"),
  0x02f21: (148, "FixedDoubleArrayMap"),
  0x02f71: (134, "MutableHeapNumberMap"),
  0x02fc1: (173, "OrderedHashMapMap"),
  0x03011: (173, "OrderedHashSetMap"),
  0x03061: (173, "NameDictionaryMap"),
  0x030b1: (173, "GlobalDictionaryMap"),
  0x03101: (173, "NumberDictionaryMap"),
  0x03151: (173, "StringTableMap"),
  0x031a1: (173, "WeakHashTableMap"),
  0x031f1: (171, "SloppyArgumentsElementsMap"),
  0x03241: (182, "SmallOrderedHashMapMap"),
  0x03291: (183, "SmallOrderedHashSetMap"),
  0x032e1: (176, "CodeDataContainerMap"),
  0x03331: (33295, "JSMessageObjectMap"),
  0x03381: (33281, "ExternalMap"),
  0x033d1: (137, "BytecodeArrayMap"),
  0x03421: (171, "ModuleInfoMap"),
  0x03471: (175, "NoClosuresCellMap"),
  0x034c1: (175, "OneClosureCellMap"),
  0x03511: (175, "ManyClosuresCellMap"),
  0x03561: (179, "PropertyArrayMap"),
  0x035b1: (130, "BigIntMap"),
  0x03601: (106, "NativeSourceStringMap"),
  0x03651: (64, "StringMap"),
  0x036a1: (73, "ConsOneByteStringMap"),
  0x036f1: (65, "ConsStringMap"),
  0x03741: (77, "ThinOneByteStringMap"),
  0x03791: (69, "ThinStringMap"),
  0x037e1: (67, "SlicedStringMap"),
  0x03831: (75, "SlicedOneByteStringMap"),
  0x03881: (66, "ExternalStringMap"),
  0x038d1: (82, "ExternalStringWithOneByteDataMap"),
  0x03921: (74, "ExternalOneByteStringMap"),
  0x03971: (98, "ShortExternalStringMap"),
  0x039c1: (114, "ShortExternalStringWithOneByteDataMap"),
  0x03a11: (0, "InternalizedStringMap"),
  0x03a61: (2, "ExternalInternalizedStringMap"),
  0x03ab1: (18, "ExternalInternalizedStringWithOneByteDataMap"),
  0x03b01: (10, "ExternalOneByteInternalizedStringMap"),
  0x03b51: (34, "ShortExternalInternalizedStringMap"),
  0x03ba1: (50, "ShortExternalInternalizedStringWithOneByteDataMap"),
  0x03bf1: (42, "ShortExternalOneByteInternalizedStringMap"),
  0x03c41: (106, "ShortExternalOneByteStringMap"),
  0x03c91: (140, "FixedUint8ArrayMap"),
  0x03ce1: (139, "FixedInt8ArrayMap"),
  0x03d31: (142, "FixedUint16ArrayMap"),
  0x03d81: (141, "FixedInt16ArrayMap"),
  0x03dd1: (144, "FixedUint32ArrayMap"),
  0x03e21: (143, "FixedInt32ArrayMap"),
  0x03e71: (145, "FixedFloat32ArrayMap"),
  0x03ec1: (146, "FixedFloat64ArrayMap"),
  0x03f11: (147, "FixedUint8ClampedArrayMap"),
  0x03f61: (169, "Tuple2Map"),
  0x03fb1: (167, "ScriptMap"),
  0x04001: (160, "InterceptorInfoMap"),
  0x04051: (151, "AccessorInfoMap"),
  0x040a1: (150, "AccessCheckInfoMap"),
  0x040f1: (152, "AccessorPairMap"),
  0x04141: (153, "AliasedArgumentsEntryMap"),
  0x04191: (154, "AllocationMementoMap"),
  0x041e1: (155, "AllocationSiteMap"),
  0x04231: (156, "AsyncGeneratorRequestMap"),
  0x04281: (157, "ContextExtensionMap"),
  0x042d1: (158, "DebugInfoMap"),
  0x04321: (159, "FunctionTemplateInfoMap"),
  0x04371: (161, "ModuleInfoEntryMap"),
  0x043c1: (162, "ModuleMap"),
  0x04411: (163, "ObjectTemplateInfoMap"),
  0x04461: (164, "PromiseReactionJobInfoMap"),
  0x044b1: (165, "PromiseResolveThenableJobInfoMap"),
  0x04501: (166, "PrototypeInfoMap"),
  0x04551: (168, "StackFrameInfoMap"),
  0x045a1: (170, "Tuple3Map"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("OLD_SPACE", 0x02201): "NullValue",
  ("OLD_SPACE", 0x02231): "EmptyDescriptorArray",
  ("OLD_SPACE", 0x02251): "EmptyFixedArray",
  ("OLD_SPACE", 0x02261): "UninitializedValue",
  ("OLD_SPACE", 0x022e1): "UndefinedValue",
  ("OLD_SPACE", 0x02311): "NanValue",
  ("OLD_SPACE", 0x02321): "TheHoleValue",
  ("OLD_SPACE", 0x02371): "HoleNanValue",
  ("OLD_SPACE", 0x02381): "TrueValue",
  ("OLD_SPACE", 0x023f1): "FalseValue",
  ("OLD_SPACE", 0x02441): "empty_string",
  ("OLD_SPACE", 0x02459): "EmptyScopeInfo",
  ("OLD_SPACE", 0x02469): "ArgumentsMarker",
  ("OLD_SPACE", 0x024c1): "Exception",
  ("OLD_SPACE", 0x02519): "TerminationException",
  ("OLD_SPACE", 0x02579): "OptimizedOut",
  ("OLD_SPACE", 0x025d1): "StaleRegister",
  ("OLD_SPACE", 0x02651): "EmptyByteArray",
  ("OLD_SPACE", 0x02661): "EmptyFixedUint8Array",
  ("OLD_SPACE", 0x02681): "EmptyFixedInt8Array",
  ("OLD_SPACE", 0x026a1): "EmptyFixedUint16Array",
  ("OLD_SPACE", 0x026c1): "EmptyFixedInt16Array",
  ("OLD_SPACE", 0x026e1): "EmptyFixedUint32Array",
  ("OLD_SPACE", 0x02701): "EmptyFixedInt32Array",
  ("OLD_SPACE", 0x02721): "EmptyFixedFloat32Array",
  ("OLD_SPACE", 0x02741): "EmptyFixedFloat64Array",
  ("OLD_SPACE", 0x02761): "EmptyFixedUint8ClampedArray",
  ("OLD_SPACE", 0x02781): "EmptyScript",
  ("OLD_SPACE", 0x02809): "UndefinedCell",
  ("OLD_SPACE", 0x02819): "EmptySloppyArgumentsElements",
  ("OLD_SPACE", 0x02839): "EmptySlowElementDictionary",
  ("OLD_SPACE", 0x02881): "EmptyOrderedHashMap",
  ("OLD_SPACE", 0x028a9): "EmptyOrderedHashSet",
  ("OLD_SPACE", 0x028d1): "EmptyPropertyCell",
  ("OLD_SPACE", 0x028f9): "EmptyWeakCell",
  ("OLD_SPACE", 0x02969): "NoElementsProtector",
  ("OLD_SPACE", 0x02991): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x029a1): "SpeciesProtector",
  ("OLD_SPACE", 0x029c9): "StringLengthProtector",
  ("OLD_SPACE", 0x029d9): "FastArrayIterationProtector",
  ("OLD_SPACE", 0x029e9): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x02a11): "ArrayBufferNeuteringProtector",
  ("OLD_SPACE", 0x02a39): "InfinityValue",
  ("OLD_SPACE", 0x02a49): "MinusZeroValue",
  ("OLD_SPACE", 0x02a59): "MinusInfinityValue",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "WASM_TO_WASM",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
