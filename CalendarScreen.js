import React, { useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Calendar } from 'react-native-calendars';

const CalendarScreen = () => {
  const [selectedDate, setSelectedDate] = useState('');

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Period Calendar</Text>
      <Calendar
        onDayPress={(day) => {
          setSelectedDate(day.dateString);
        }}
        markedDates={{
          [selectedDate]: { selected: true, selectedColor: 'pink' },
        }}
      />
      {selectedDate ? (
        <Text style={styles.selectedDate}>Selected Date: {selectedDate}</Text>
      ) : null}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  selectedDate: {
    marginTop: 20,
    fontSize: 18,
    color: 'gray',
  },
});

export default CalendarScreen;
