package edu.illinois.storm;

import org.apache.storm.redis.common.mapper.RedisDataTypeDescription;
import org.apache.storm.redis.common.mapper.RedisStoreMapper;
import org.apache.storm.tuple.ITuple;

public class TopNStoreMapper implements RedisStoreMapper {
  private RedisDataTypeDescription description;
  private final String hashKey;

  public TopNStoreMapper(String hashKey) {
    this.hashKey = hashKey;
    description =
        new RedisDataTypeDescription(RedisDataTypeDescription.RedisDataType.HASH, hashKey);
  }

  @Override
  public RedisDataTypeDescription getDataTypeDescription() {
    return description;
  }

  @Override
  public String getKeyFromTuple(ITuple tuple) {
    /* ----------------------TODO-----------------------
    Task: define which part of the tuple as the key
    ------------------------------------------------- */
    // return "hashKey_" + tuple.getString(0);
    return tuple.getStringByField("top-N");
		// End
  }

  @Override
  public String getValueFromTuple(ITuple tuple) {
    /* ----------------------TODO-----------------------
    Task: define which part of the tuple as the value
    ------------------------------------------------- */
    // return tuple.getInteger(1).toString();
    return tuple.getStringByField("word");
    // return String.valueOf(tuple.getLongByField("value"));
		// End
  }
}
