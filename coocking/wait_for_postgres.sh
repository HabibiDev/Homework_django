if [ -z "$DATABASE_URL" ]; then
    echo "Missing database url"
    exit 2
fi

RETRIES="${RETRIES:-10}"

echo -n "Waiting for postgres..."

if ! which psql > /dev/null; then
    echo 'PSQL_MISSING'
    exit 3
fi

until psql "$DATABASE_URL" -c "select 1" > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
  echo -n  " $((RETRIES--))"
  sleep 1
done

if [ $RETRIES -le 0 ]; then
    echo " TIME_OUT"
    exit 1
else
    echo " OK"
    exit 0
fi