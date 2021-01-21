from .mania_holdnote_hitobject_base import ManiaHoldNoteHitobjectBase


class ManiaHoldNoteIO():

    @staticmethod
    def load_holdnote(data, difficulty):
        holdnote = ManiaHoldNoteHitobjectBase()
        if not data: return holdnote

        ManiaHoldNoteIO.__process_holdnote_data(data, holdnote, difficulty)

        return holdnote


    @staticmethod
    def __process_holdnote_data(data, holdnote, difficulty):
        holdnote.pos            = [ int(data[0]), int(data[1]) ]
        holdnote.time           = int(data[2])
        holdnote.hitobject_type = int(data[3])
        
        slider_data = data[5].split(':')
        holdnote.end_time = int(slider_data[0])

        holdnote.difficulty = difficulty